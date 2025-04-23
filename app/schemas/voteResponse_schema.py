from pydantic import BaseModel

class VoteOut(BaseModel):
    id: str
    voter_id: str
    candidate_id: str

    class Config:
        orm_mode = True
