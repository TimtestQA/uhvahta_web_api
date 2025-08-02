from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class LegalData(BaseModel):
    inn: str
    name: str


class Subscription(BaseModel):
    tariff_name: str
    auto_renewal: bool
    end_date: datetime
    renewal_date: datetime
    renewal_amount: int
    subscription_id: int
    tariff_id: int


class RecruiterProfileModel(BaseModel):
    phone: str
    fio: str
    legal_data: LegalData | None = None
    person_type: str
    email: EmailStr
    id: int
    has_subscription: bool
    subscription: Optional[Subscription]