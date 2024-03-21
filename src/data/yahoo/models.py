from pydantic import BaseModel
from typing import Optional

class FuturePrice(BaseModel):
    date: str
    close: float 
