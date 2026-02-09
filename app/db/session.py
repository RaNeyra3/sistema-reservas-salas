# app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexión para MySQL (XAMPP por defecto: usuario root sin contraseña)
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/reservas_db"

engine = create_engine(
    DATABASE_URL,
    echo=False,          # Cambia a True si quieres ver queries en consola
    future=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# app/db/session.py (agregar al final)
from typing import Generator

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
