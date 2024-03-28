from dataclasses import dataclass
from datetime import date

@dataclass
class Payment:
    amount: float
    currency: str
    date: date
    payment_type: str
    items: list = []