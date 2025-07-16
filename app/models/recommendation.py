from pydantic import BaseModel
from typing import List, Optional

class GiftRequest(BaseModel):
    birth_date: str
    gender: str
    age: int
    job: str
    relationship: str
    price_min: int
    price_max: int
    prompt: str = ""

class GiftItem(BaseModel):
    product_name : str
    approx_price_krw : int
    reason : str

class GiftResponse(BaseModel):
    recommendations: List[GiftItem]