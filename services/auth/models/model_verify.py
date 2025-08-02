from pydantic import BaseModel, EmailStr

class VerifyOrContinueModel(BaseModel):
    email: EmailStr
    otp_code: str 