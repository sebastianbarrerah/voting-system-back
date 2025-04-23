from pydantic import BaseModel
from typing import Optional

class CandidateCreate(BaseModel):
    name: str
    party: Optional[str] = None

class CandidateResponse(BaseModel):
    id: str
    name: str
    party: Optional[str]
    votes: int

    class Config:
        orm_mode = True
