from uuid import UUID
from pydantic import BaseModel
from typing import Optional

class VoterCreate(BaseModel):
    name: str
    email: str
    password: Optional[str] = None

class VoterResponse(BaseModel):
    id: UUID
    name: str
    email: str
    password: Optional[str] = None
    hasVoted: bool

    class Config:
        from_attributes = True
