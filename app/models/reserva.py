# app/models/reserva.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.session import Base

class Reserva(Base):
    __tablename__ = "reservas"

    id_reserva = Column(Integer, primary_key=True, index=True)

    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_sala = Column(Integer, ForeignKey("salas.id_sala"), nullable=False)

    horario = Column(String(30), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relaciones ORM (opcional, pero recomendado)
    usuario = relationship("Usuario")
    sala = relationship("Sala")
