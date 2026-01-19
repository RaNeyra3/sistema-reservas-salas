# app/main.py
from fastapi import FastAPI
from .reservas.schemas import ReservaCreate
from .reservas.service import crear_reserva

app = FastAPI(
    title="Sistema de Reservas de Salas",
    version="1.0.0"
)

@app.get("/ping")
def ping():
    return {
        "status": "ok",
        "message": "API funcionando correctamente"
    }

@app.post("/reservas")
def crear_reserva_endpoint(reserva: ReservaCreate):
    ok = crear_reserva(
        usuario_id=reserva.usuario_id,
        sala_id=reserva.sala_id,
        horario=reserva.horario
    )

    if not ok:
        return {"ok": False, "error": "Datos inválidos"}

    return {"ok": True, "message": "Reserva creada correctamente"}