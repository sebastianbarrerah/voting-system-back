from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database import Base
from sqlalchemy.orm import relationship

class Candidate(Base):
    __tablename__ = "candidates"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    party = Column(String, nullable=True)
    votes = Column(Integer, default=0)
    
    votes_received = relationship("Vote", back_populates="candidate")