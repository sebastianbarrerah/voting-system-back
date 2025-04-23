from pydantic import BaseModel
from uuid import UUID

class VoteCreate(BaseModel):
    voter_id: str
    candidate_id: str

class VoteResponse(BaseModel):
    id: UUID
    voter_id: UUID
    candidate_id: UUID

    class Config:
        from_attributes = True 