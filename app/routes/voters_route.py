from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from app.database import get_db
from app.models.voter_model import Voter
from app.schemas.voter_schema import VoterCreate, VoterResponse
from app.models.candidate_model import Candidate

voter_routes = APIRouter()


@voter_routes.post("/voters", response_model=VoterResponse)
def create_voter(voter: VoterCreate, db: Session = Depends(get_db)):
    existing_voter = db.query(Voter).filter(Voter.email == voter.email).first()
    if existing_voter:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El email ya está registrado",
        )

    db_voter = Voter(name=voter.name, email=voter.email, password=voter.password)

    db.add(db_voter)
    db.commit()
    db.refresh(db_voter)
    return db_voter


@voter_routes.get(
    "/voters",
    response_model=List[VoterResponse],
    summary="Obtener lista de votantes",
    description="Retorna una lista paginada de todos los votantes registrados.",
)
async def get_voters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    voters = db.query(Voter).offset(skip).limit(limit).all()
    return voters


@voter_routes.get(
    "/voters/{voter_id}",
    response_model=VoterResponse,
    summary="Obtener detalles de un votante",
    description="Informarción del votante por el id.",
)
async def get_voter(voter_id: UUID, db: Session = Depends(get_db)):
    db_voter = db.query(Voter).filter(Voter.id == voter_id).first()

    if not db_voter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Votante no encontrado"
        )

    return db_voter


@voter_routes.delete(
    "/voters/{voter_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un votante",
    description="Elimina un votante por su id.",
)
async def delete_voter(voter_id: UUID, db: Session = Depends(get_db)):
    db_voter = db.query(Voter).filter(Voter.id == voter_id).first()
    if not db_voter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Votante no encontrado"
        )

    if db_voter.hasVoted:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se puede eliminar un votante que ya ha votado",
        )

    db.delete(db_voter)
    db.commit()

    return None


@voter_routes.get(
    "/voters/email/{email}",
    response_model=VoterResponse,
    summary="Buscar votante por email",
    description="Obtiene un votante por email",
    tags=["busquedas"],
)
async def get_voter_by_email(email: str, db: Session = Depends(get_db)):
    db_voter = db.query(Voter).filter(Voter.email == email).first()

    if not db_voter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Votante no encontrado"
        )

    return db_voter


@voter_routes.get(
    "/voters/has-voted/{voter_id}",
    response_model=bool,
    summary="Verificar si un votante ha votado",
    description="Retorna true/false indicando si el votante ha emitido su voto.",
)
async def check_has_voted(voter_id: UUID, db: Session = Depends(get_db)):
    db_voter = db.query(Voter).filter(Voter.id == voter_id).first()

    if not db_voter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Votante no encontrado"
        )

    return db_voter.hasVoted
