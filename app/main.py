from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base

Base.metadata.crete_all(bind=engine)

app = FastAPI(
    title="Smart Finance Management System",
    description="AI-Powered Finance Tracker using FastAPI, PostgreSQL, and Groq AI",
    version="1.0.0"
)

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
def read_root():
    return {
        'message': 'Smart Finance API is running!',
        'status': "healthy"
    }

@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'database': 'connected'
    }