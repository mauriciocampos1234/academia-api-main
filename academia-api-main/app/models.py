from sqlalchemy import Column, Integer, String
from .database import Base


class Participante(Base):
    __tablename__ = "participantes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    idade = Column(Integer, nullable=True)
    centro_treinamento = Column(String(100))
    categoria = Column(String(50))