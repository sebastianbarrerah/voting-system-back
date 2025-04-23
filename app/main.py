from fastapi import FastAPI  
from app.database import Base, engine
from app.routes.voters_route import voter_routes
from app.routes.candidates_route import candidate_routes
from app.routes.votes_route import vote_routes

app = FastAPI()

app.include_router(voter_routes, prefix="/api", tags=["Voters"])
app.include_router(candidate_routes, prefix="/api", tags=["Candidates"])
app.include_router(vote_routes, prefix="/api", tags=["Votes"])

@app.on_event("startup")
async def startup():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"mensaje": "Hola mundo"}