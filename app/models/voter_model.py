
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from app.database import Base
from sqlalchemy.orm import relationship

class Voter(Base):
    __tablename__ = "voters"

    id = Column(String, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String, unique=True, index=True)
    hasVoted = Column(Boolean, default=False)
    password = Column(String, nullable=True)
    created_at = Column(DateTime)
    votes = relationship("Vote", back_populates="voter")