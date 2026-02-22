import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ddgs import DDGS
from groq import Groq
import logging
import os

# Suppress debug logs from libraries
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("groq").setLevel(logging.WARNING)
logging.getLogger("ddgs").setLevel(logging.WARNING)

# Configure logging for our app only
log_path = os.path.join(os.path.dirname(__file__), "messages.txt")
logging.basicConfig(
    filename=log_path, 
    level=logging.INFO, 
    format='%(message)s',
    filemode='a'  # Append mode
)

# Remove any existing handlers and set fresh ones
logger = logging.getLogger()
logger.handlers = []

# File handler
file_handler = logging.FileHandler(log_path, mode='a')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

# Initialize Groq client
client = Groq(
    api_key="##YOUR_GROQ_API_KEY##"
)

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    message: str

# Store conversation history
conversation_history = []

def perform_search(query):
    """Searches the web and returns the top 3 results summary."""
    try:
        results = DDGS().text(query, max_results=3)
        if not results:
            return "No search results found."

        context = "Search Results:\n"
        for res in results:
            context += f"- Title: {res['title']}\n Snippet: {res['body']}\n Link: {res['href']}\n\n"
        return context
    except Exception as e:
        return "Could not perform search."

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.message
    
    try:
        search_context = perform_search(user_message)

        system_prompt = (
                "#PROMPT HERE "
                "#PROMPT HERE "
                "#PROMPT HERE "
        )

        # Build messages list for Groq API
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "system", "content": f"Relevant context from search: {search_context}"}
        ]

        # Add conversation history
        messages.extend(conversation_history)

        # Add current user message
        messages.append({"role": "user", "content": user_message})

        # Call Groq API
        response = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
        )

        # Extract response content
        ai_response = response.choices[0].message.content

        # Add to conversation history
        conversation_history.append({"role": "user", "content": user_message})
        conversation_history.append({"role": "assistant", "content": ai_response})

        # Log the exchange
        logging.info(f"Sent: {user_message}")
        logging.info(f"Response: {ai_response}")

        return {"response": ai_response, "context_used": search_context}

    except Exception as e:
        error_message = f"Error: {str(e)}"
        logging.error(error_message)
        return {
            "response": error_message,
            "context_used": ""
        }

if __name__ == "__main__":
    print("Starting Server...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
