from datetime import date
from typing import Optional, List
from pydantic import BaseModel, EmailStr, validator
import re

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

    @validator("password")
    def validate_password(cls, v):
        if len(v) < 8 or len(v) > 20:
            raise ValueError("Password must be between 8 and 20 characters")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one number")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password must contain at least one special character")
        weak_list = ["password", "12345678", "qwerty", "letmein", "admin", "welcome"]
        if v.lower() in weak_list:
            raise ValueError("Password is too easy")
        return v

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True

class ExpenseBase(BaseModel):
    amount: float
    description: Optional[str] = None
    date: date
    category_id: int

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseUpdate(BaseModel):
    amount: Optional[float] = None
    description: Optional[str] = None
    date: Optional[date] = None
    category_id: Optional[int] = None

class ExpenseOut(ExpenseBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True
