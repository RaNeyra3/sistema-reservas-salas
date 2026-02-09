# app/models/sala.py
from sqlalchemy import Column, Integer, String, Boolean
from app.db.session import Base

class Sala(Base):
    __tablename__ = "salas"

    id_sala = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(80), nullable=False)
    capacidad = Column(Integer, nullable=False)
    disponible = Column(Boolean, default=True, nullable=False)
