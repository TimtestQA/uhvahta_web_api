from pydantic import BaseModel
from typing import List, Optional

class RespondItem(BaseModel):
    id: int
    # Добавь остальные поля по swagger

class RespondsResponseModel(BaseModel):
    items: List[RespondItem]
    total: Optional[int] 