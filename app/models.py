from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

# 1. USER MODEL
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    accounts = relationship("Account", back_populates="owner")
    budgets = relationship("Budget", back_populates="owner")

# 2. ACCOUNT MODEL (Bank, Cash, Credit Card, etc.)
class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    account_type = Column(String(50), nullable=False) # e.g., 'Bank', 'Cash', 'Credit Card'
    name = Column(String(100), nullable=False) # e.g., 'HBL Checking', 'Meezan Savings'
    balance = Column(Float, default=0.0)
    
    # Relationships
    owner = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")

# 3. CATEGORY MODEL (Food, Rent, Salary, etc.)
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    type = Column(String(20), nullable=False) # 'income' or 'expense'
    is_ai_generated = Column(Boolean, default=False) # Agar Groq ne auto-create ki ho

# 4. TRANSACTION MODEL (The Core of Finance App)
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    
    amount = Column(Float, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())
    description = Column(Text, nullable=True) # e.g., 'Uber ride to office'
    merchant_name = Column(String(150), nullable=True) # e.g., 'Uber', 'KFC'
    
    is_recurring = Column(Boolean, default=False) # Subscription ya monthly bill?
    
    # 🌟 PRO FEATURE: Groq AI Metadata (JSONB)
    # Yahan AI apni tags, confidence score, ya suggestions save karega
    ai_metadata = Column(JSON, nullable=True) 

    # Relationships
    account = relationship("Account", back_populates="transactions")
    category = relationship("Category")

# 5. BUDGET MODEL
class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    
    monthly_limit = Column(Float, nullable=False)
    spent_amount = Column(Float, default=0.0) # Yeh hum baad mein update karenge

    # Relationships
    owner = relationship("User", back_populates="budgets")
    category = relationship("Category")