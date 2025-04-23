from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database import Base

class Voter(Base):
    __tablename__ = "voters"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=True)  
    hasVoted = Column(Boolean, default=False)
    

    votes_cast = relationship("Vote", back_populates="voter")