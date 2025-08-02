from pydantic import BaseModel, EmailStr

class SendOTPModel(BaseModel):
    email: EmailStr 