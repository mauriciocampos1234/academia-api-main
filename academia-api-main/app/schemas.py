from pydantic import BaseModel

class ParticipanteBase(BaseModel):
    nome: str
    cpf: str
    idade: int | None = None
    centro_treinamento: str | None = None

class ParticipanteCreate(ParticipanteBase):
    pass

class ParticipanteOut(BaseModel):
    nome: str
    idade: int | None = None
    centro_treinamento: str | None = None
    categoria: str | None = None

    model_config = {
        "from_attributes": True
    }
