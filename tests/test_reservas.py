# tests/test_reservas.py
from app.models.usuario import Usuario
from app.models.sala import Sala

def test_crear_reserva_valida(client, db_session):
    # Seed mínimo en BD de test
    db_session.add(Usuario(id_usuario=1, nombre="User Test", correo="test@test.com", activo=True))
    db_session.add(Sala(id_sala=1, nombre="Sala Test", capacidad=10, disponible=True))
    db_session.commit()

    payload = {
        "usuario_id": 1,
        "sala_id": 1,
        "horario": "10:00-11:00"
    }

    response = client.post("/reservas", json=payload)
    assert response.status_code == 200
    assert response.json()["ok"] is True

def test_crear_reserva_invalida(client, db_session):
    # Seed mínimo (para que no falle por FK)
    db_session.add(Usuario(id_usuario=1, nombre="User Test", correo="test2@test.com", activo=True))
    db_session.add(Sala(id_sala=1, nombre="Sala Test", capacidad=10, disponible=True))
    db_session.commit()

    payload = {
        "usuario_id": 0,
        "sala_id": 1,
        "horario": "10:00-11:00"
    }

    response = client.post("/reservas", json=payload)
    assert response.status_code == 200
    assert response.json()["ok"] is False
    assert "error" in response.json()

def test_crear_reserva_error_validacion_422(client):
    payload = {
        "usuario_id": "texto",
        "sala_id": 1,
        "horario": "10:00-11:00"
    }

    response = client.post("/reservas", json=payload)
    assert response.status_code == 422