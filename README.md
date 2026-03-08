# ⚡ Fast-Groq AI Chatbot
> A high-performance AI chat interface using FastAPI, Groq, and DuckDuckGo search integration.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi&logoColor=white)
![Groq](https://img.shields.io/badge/AI-Groq-orange)

This project is a full-stack AI chatbot. It features a modern HTML/JS frontend and a Python backend powered by **FastAPI**. It doesn't just talk—it can search the web using the DuckDuckGo Search (DDGS) integration!

## ✨ Features
* **Lightning Fast:** Uses Groq's LPU inference for instant replies.
* **Web Search:** Integrated `duckduckgo-search` to find real-time info.
* **Modern Backend:** Built with FastAPI for high-performance asynchronous handling.
* **CORS Ready:** Pre-configured to work with your local frontend.

## 🛠 Setup & Installation

### 1. Install Dependencies
You need Python installed. Run this command to install all the necessary libraries:
```bash
pip install fastapi uvicorn pydantic duckduckgo-search groq
