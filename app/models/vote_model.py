from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base

class Vote(Base):
    __tablename__ = "votes"

    id = Column(String, primary_key=True, index=True)
    voter_id = Column(String, ForeignKey("voters.id"), nullable=False)
    candidate_id = Column(String, ForeignKey("candidates.id"), nullable=False)

    voter = relationship("Voter", backref="votes")
    candidate = relationship("Candidate", backref="votes")