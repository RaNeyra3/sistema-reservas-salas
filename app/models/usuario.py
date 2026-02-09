# app/models/usuario.py
from sqlalchemy import Column, Integer, String, Boolean
from app.db.session import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(120), unique=True, nullable=False)
    activo = Column(Boolean, default=True, nullable=False)
