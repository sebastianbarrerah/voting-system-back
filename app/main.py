from fastapi import FastAPI  
from app.models.candidate_model import Candidate  # type: ignore # noqa: F401
from app.models.voter_model import Voter  # type: ignore # noqa: F401
from app.models.vote_model import Vote # type: ignore  # noqa: F401
from app.database import Base, engine


app = FastAPI()


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}
    