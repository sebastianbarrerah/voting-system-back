from app.database import Base
from sqlalchemy import Column, Integer, String

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(String, primary_key=True, index=True)
    name = Column(String(100), index=True)
    party = Column(String(50), index=True, nullable=True)
    votes = Column(Integer, default=0)
    