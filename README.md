# ⚡ Fast-Groq AI Chatbot
> A high-performance AI chat interface using FastAPI, Groq, and DuckDuckGo search integration.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi&logoColor=white)
![Groq](https://img.shields.io/badge/AI-Groq-orange)

This project is a full-stack AI chatbot. It features a modern HTML/JS frontend and a Python backend powered by **FastAPI**. It doesn't just talk—it can search the web using the DuckDuckGo Search (DDGS) integration!

---

## ✨ Features
* **Lightning Fast:** Uses Groq's LPU inference for instant replies.
* **Web Search:** Integrated `duckduckgo-search` to find real-time info.
* **Modern Backend:** Built with FastAPI for high-performance asynchronous handling.
* **CORS Ready:** Pre-configured to work with your local frontend.

---

## 🛠 Installation & Setup

### 1. Install Dependencies
You must have Python installed. Run this command to install all the necessary libraries for the server:
  BASH:
pip install fastapi uvicorn pydantic duckduckgo-search groq

2. Configure your API Key
Open your Python file and locate the Groq client initialization. Replace the placeholder with your actual key:

Python

client = Groq(api_key="your_groq_api_key_here")
Note: Keep this key secret! Do not share it publicly or commit it to GitHub.

##🚀 How to Run
1. Start the Backend
Start the FastAPI server using uvicorn:

Bash

uvicorn your_filename_here:app --reload
(Replace your_filename_here with the name of your Python file, e.g., main if your file is main.py)

2. Open the Frontend
Open your project folder in VS Code.

Right-click your index.html file and select "Open with Live Server".

##📜 License & Warranty
This project is licensed under the MIT License.

What this means: You are free to use, copy, modify, and distribute this software for any purpose (even commercially) as long as you include the original copyright notice.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. The author is not liable for any issues, data leaks (if you expose your API key), or damages arising from the use of this code.

See the LICENSE file for the full legal text.


Would you like me to put the **CoinFlip** or the **Hologram** project into this exact same "one-block" format next?
