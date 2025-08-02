from pydantic import BaseModel, EmailStr
from typing import Optional, LiteralString, Literal
from datetime import datetime


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


class RecruiterDataModel(BaseModel):
    phone: str
    fio: str
    legal_data: LegalData
    person_type: Literal["Организация", "Физлицо"]
    email: EmailStr
    id: int
    has_subscription: bool
    subscription: str | None = None   # если может быть None



class CreateRecruiterResponseModel(BaseModel):
    token_type: str
    access_token: str
    refresh_token: str