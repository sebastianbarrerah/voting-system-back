from pydantic import BaseModel

class VoteCreate(BaseModel):
    voter_id: str
    candidate_id: str
