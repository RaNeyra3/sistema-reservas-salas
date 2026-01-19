from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_reserva_valida():
    payload = {
        "usuario_id": 1,
        "sala_id": 2,
        "horario": "10:00-11:00"
    }

    response = client.post("/reservas", json=payload)
    assert response.status_code == 200
    assert response.json()["ok"] is True

def test_crear_reserva_invalida():
    payload = {
        "usuario_id": 0,
        "sala_id": 2,
        "horario": "10:00-11:00"
    }

    response = client.post("/reservas", json=payload)

    assert response.status_code == 200
    assert response.json()["ok"] is False
    assert "error" in response.json()

def test_crear_reserva_error_validacion_422():
    payload = {
        "usuario_id": "texto",
        "sala_id": 2,
        "horario": "10:00-11:00"
    }

    response = client.post("/reservas", json=payload)

    assert response.status_code == 422
