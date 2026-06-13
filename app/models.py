from pydantic import BaseModel
from datetime import datetime

class Trade(BaseModel):
    symbol: str
    entry_time: datetime
    exit_time: datetime
    entry_price: float
    exit_price: float
    volume: float
    profit: float