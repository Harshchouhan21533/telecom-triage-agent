# Telecom Support Triage Agent 🤖

## 📌 Overview
AI-powered telecom support system using local LLM (Ollama + Gemma3:1B).

## 🚀 Features
- Intent Classification (billing, network, etc.)
- Urgency Detection
- Named Entity Recognition
- AI Response Generation
- Chat Memory (multi-turn conversation)
- Streamlit UI

## 🛠 Tech Stack
- Python
- FastAPI
- Streamlit
- Ollama (Gemma3:1B)
- LangChain
- spaCy

## ▶️ How to Run

### 1. Start Ollama
ollama run gemma3:1b

### 2. Start Backend
python -m uvicorn app:app --reload

### 3. Start UI
python -m streamlit run streamlit_app.py
