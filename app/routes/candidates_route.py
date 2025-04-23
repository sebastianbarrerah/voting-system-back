from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.voter_model import Voter
from app.models.candidate_model import Candidate
from app.schemas.candidate_schema import CandidateCreate, CandidateResponse
from uuid import UUID

candidate_routes = APIRouter()

@candidate_routes.post("/candidates", response_model=CandidateResponse)
def create_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):
    existingInVolter = db.query(Voter).filter(Voter.email == candidate.email).first()
    if existingInVolter:
        raise HTTPException(status_code=400, detail="El email ya esta registrado como votante")
    
    db_candidate = Candidate(**candidate.dict())
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate

@candidate_routes.get("/candidates", response_model=list[CandidateResponse])
def read_candidates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    candidates = db.query(Candidate).offset(skip).limit(limit).all()
    return candidates

@candidate_routes.get("/candidates/{candidate_id}", response_model=CandidateResponse)
def read_candidate(candidate_id: UUID, db: Session = Depends(get_db)):
    db_candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    if db_candidate is None:
        raise HTTPException(status_code=404, detail="candidato no encontrado")
    return db_candidate

@candidate_routes.delete("/candidates/{candidate_id}")
def delete_candidate(candidate_id: UUID, db: Session = Depends(get_db)):
    db_candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    if db_candidate is None:
        raise HTTPException(status_code=404, detail="candidato no encontrado")
    db.delete(db_candidate)
    db.commit()
    return {"message": "Candidato eliminado correctamente"}