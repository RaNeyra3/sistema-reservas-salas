from pydantic import BaseModel

class ReservaCreate(BaseModel):
    usuario_id: int
    sala_id: int
    horario: str
