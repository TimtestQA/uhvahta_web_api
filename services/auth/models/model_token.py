from pydantic import BaseModel
from typing import Optional

class TokenResponseModel(BaseModel):
    token_type: Optional[str] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    registered: Optional[bool] = None 