from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, init_db
from .models import Order
from .schemas import OrderCreate

router = APIRouter()

# 初始化数据库
init_db()


# Dependency to get the database session in API endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db  # Provide a session
    finally:
        db.close()  # Close session after use


# submit a new order
@router.post("/orders")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = Order(**order.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


# get all orders
@router.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()
