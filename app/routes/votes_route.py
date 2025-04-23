from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Vote, Voter, Candidate
from app.schemas.vote_schema import VoteCreate, VoteResponse 
from uuid import UUID

vote_routes = APIRouter()

@vote_routes.post("/votes", response_model=VoteResponse)
def create_vote(vote: VoteCreate, db: Session = Depends(get_db)):
    db_voter = db.query(Voter).filter(Voter.id == UUID(vote.voter_id)).first()
    if not db_voter:
        raise HTTPException(status_code=404, detail="votante no encontrado")
    
    db_candidate = db.query(Candidate).filter(Candidate.id == UUID(vote.candidate_id)).first()
    if not db_candidate:
        raise HTTPException(status_code=404, detail="candiato no encontrado")
    
    if db_voter.hasVoted:
        raise HTTPException(status_code=400, detail="votante ya ha votado")
    
    if db.query(Candidate).filter(Candidate.id == UUID(vote.voter_id)).first():
        raise HTTPException(status_code=400, detail="Votante no puede votar por sí mismo")
    
    db_vote = Vote(
        voter_id=UUID(vote.voter_id),
        candidate_id=UUID(vote.candidate_id)
    )
    
    db_voter.hasVoted = True
    
    db_candidate.votes += 1
    
    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return db_vote

@vote_routes.get("/votes", response_model=list[VoteResponse])
def read_votes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    votes = db.query(Vote).offset(skip).limit(limit).all()
    return votes

@vote_routes.get("/votes/statistics")
def get_vote_statistics(db: Session = Depends(get_db)):
    candidates = db.query(Candidate).all()
    total_votes = db.query(Vote).count()
    
    statistics = []
    for candidate in candidates:
        percentage = (candidate.votes / total_votes) * 100 if total_votes > 0 else 0
        statistics.append({
            "candidate_id": str(candidate.id),
            "candidate_name": candidate.name,
            "party": candidate.party,
            "votes": candidate.votes,
            "percentage": round(percentage, 2)
        })
    
    voters_voted = db.query(Voter).filter(Voter.hasVoted is True).count()
    
    return {
        "statistics": statistics,
        "total_votes": total_votes,
        "voters_voted": voters_voted
    }