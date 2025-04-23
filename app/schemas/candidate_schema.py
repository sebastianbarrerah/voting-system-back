from uuid import UUID
from pydantic import BaseModel
from typing import Optional

class CandidateCreate(BaseModel):
    name: str
    email: str
    party: Optional[str] = None

class CandidateResponse(BaseModel):
    id: UUID
    name: str
    email: str
    party: Optional[str]
    votes: int

    class Config:
        from_attributes = True