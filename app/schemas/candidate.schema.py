
from pydantic import BaseModel
from typing import Optional

class candidateSchema(BaseModel):
    id: str
    name: str
    party: Optional[str] = None
    votes: int = 0