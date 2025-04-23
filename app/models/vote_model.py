from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database import Base
from sqlalchemy.orm import relationship

class Vote(Base):
    __tablename__ = "votes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    voter_id = Column(UUID(as_uuid=True), ForeignKey('voters.id'))
    candidate_id = Column(UUID(as_uuid=True), ForeignKey('candidates.id'))
    
    voter = relationship("Voter", back_populates="votes_cast")
    candidate = relationship("Candidate", back_populates="votes_received")