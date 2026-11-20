from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

# --- USER SCHEMAS ---
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    # Pydantic V2 ka naya tarika ORM models ko read karne ka
    model_config = ConfigDict(from_attributes=True)

# --- TRANSACTION SCHEMAS ---
class TransactionBase(BaseModel):
    amount: float
    description: Optional[str] = None
    merchant_name: Optional[str] = None
    account_id: int
    category_id: Optional[int] = None

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    date: datetime
    is_recurring: bool
    
    model_config = ConfigDict(from_attributes=True)