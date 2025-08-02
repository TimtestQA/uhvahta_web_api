from pydantic import BaseModel

class PaymentResponseModel(BaseModel):
    # Примерные поля, уточни по swagger
    widget_url: str 