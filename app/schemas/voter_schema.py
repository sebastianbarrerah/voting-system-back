from pydantic import BaseModel
from typing import Optional

class VoterCreate(BaseModel):
    name: str
    email: str
    password: Optional[str] = None

class VoterResponse(BaseModel):
    id: int
    name: str
    email: str
    hasVoted: bool

    class Config:
        orm_mode = True
