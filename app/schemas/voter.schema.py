from pydantic import BaseModel
from typing import Optional

class VoterSchema(BaseModel):
    id: str
    name: str
    email: str
    hasVoted: bool
    password: Optional[str] = None
    created_at: str
