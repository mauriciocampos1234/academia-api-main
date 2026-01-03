from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi_pagination import LimitOffsetPage, Params
from fastapi_pagination.ext.sqlalchemy import paginate

from ..database import get_db
from ..models import Participante
from ..schemas import ParticipanteCreate, ParticipanteOut

router = APIRouter(prefix="/participantes", tags=["participante"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ParticipanteOut
)
def registrar_participante(
    payload: ParticipanteCreate,
    db: Session = Depends(get_db)
):
    participante = Participante(**payload.model_dump())
    try:
        db.add(participante)
        db.commit()
        db.refresh(participante)
        return participante
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="CPF já cadastrado",
        )


@router.get("/", response_model=LimitOffsetPage[ParticipanteOut])
def listar_participantes(
    nome: str | None = None,
    cpf: str | None = None,
    params: Params = Depends(),
    db: Session = Depends(get_db),
):
    query = db.query(Participante)

    if nome:
        query = query.filter(Participante.nome.ilike(f"%{nome}%"))

    if cpf:
        query = query.filter(Participante.cpf == cpf)

    return paginate(db, query)