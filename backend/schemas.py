from pydantic import BaseModel


class OrderCreate(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str  # "buy" or "sell"
