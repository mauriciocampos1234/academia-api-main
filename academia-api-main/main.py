from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.database import Base, engine
from app.routers import participante

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Academia API")

app.include_router(participante.router)
add_pagination(app)


@app.get("/")
def raiz():
    return {"mensagem": "Bem-vindo à Academia API!"}