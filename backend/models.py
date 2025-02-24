from sqlalchemy import Column, Integer, String, Float
from .database import Base


# Define the Order model for the database
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)  # Unique ID
    symbol = Column(String, index=True)  # Stock symbol (e.g., AAPL)
    price = Column(Float)  # Order price
    quantity = Column(Integer)  # Number of shares
    order_type = Column(String)  # Type: "buy" or "sell"
