from pydantic import BaseModel
from typing import List

class TransactionInput(BaseModel):
    Time: float
    amount: float
    V: List[float]
    velocity: int
    is_foreign: bool