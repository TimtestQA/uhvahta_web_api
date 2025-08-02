from pydantic import BaseModel
from typing import List

class TariffResponseModel(BaseModel):
    id: int
    name: str
    duration_days: int
    price: int
    discount_price: int | None = None
    features: List[str] | None = None
    short_description: str 