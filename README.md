# 💰 Smart Finance Management System

An AI-powered personal finance management system built with FastAPI, PostgreSQL, SQLAlchemy, and Groq AI.

## 🚀 Features
- Smart Auto-Categorization of transactions using Groq AI
- Chat with your finances (NLP queries)
- Budget tracking and anomaly detection
- Professional Git Workflow (Feature Branch & PR based)

## 🛠️ Tech Stack
- **Backend:** Python, FastAPI, SQLAlchemy
- **Database:** PostgreSQL
- **AI:** Groq API (Llama 3 / Mixtral)
- **Frontend:** HTML, Tailwind CSS, Vanilla JS (Claude AI Generated)

## ⚙️ Setup Instructions
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Setup `.env` file with your Database URL and Groq API Key
6. Run the server: `uvicorn app.main:app --reload`