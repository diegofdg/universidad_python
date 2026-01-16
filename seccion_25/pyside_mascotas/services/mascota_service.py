# services/mascota_service.py (MODIFICADO)
# Se agrega eliminar() sin adelantar nada más.

from database import SessionLocal
from models.mascota import Mascota


def obtener_todos():
    with SessionLocal() as session:
        return session.query(Mascota).all()


def crear(datos):
    nombre = datos.get("nombre", "").strip()
    especie = datos.get("especie", "").strip()
    peso = datos.get("peso", "").strip()

    if not nombre:
        return False, "El nombre no puede ir vacío."
    if not especie:
        return False, "La especie no puede ir vacía."

    try:
        peso_float = float(peso)
    except ValueError:
        return False, "El peso debe ser un número válido."

    with SessionLocal() as session:
        nueva = Mascota(nombre=nombre, especie=especie, peso=peso_float)
        session.add(nueva)
        session.commit()
        session.refresh(nueva)

    return True, f"Mascota '{nombre}' registrada con éxito."


def obtener_por_id(id_mascota):
    try:
        id_int = int(id_mascota)
    except ValueError:
        return None

    with SessionLocal() as session:
        return session.query(Mascota).filter(Mascota.id == id_int).first()


def actualizar(id_mascota, datos):
    nombre = datos.get("nombre", "").strip()
    especie = datos.get("especie", "").strip()
    peso = datos.get("peso", "").strip()

    if not nombre:
        return False, "El nombre no puede ir vacío."
    if not especie:
        return False, "La especie no puede ir vacía."

    try:
        peso_float = float(peso)
    except ValueError:
        return False, "El peso debe ser un número válido."

    with SessionLocal() as session:
        mascota = session.query(Mascota).filter(Mascota.id == id_mascota).first()

        if not mascota:
            return False, "La mascota no existe."

        mascota.nombre = nombre
        mascota.especie = especie
        mascota.peso = peso_float

        session.commit()

    return True, f"Mascota '{nombre}' actualizada correctamente."


def eliminar(id_mascota):   # [NUEVO]
    """Elimina una mascota existente por ID."""
    try:
        id_int = int(id_mascota)
    except ValueError:
        return False, "ID inválido."

    with SessionLocal() as session:
        mascota = session.query(Mascota).filter(Mascota.id == id_int).first()

        if not mascota:
            return False, "La mascota no existe."

        session.delete(mascota)
        session.commit()

    return True, "Mascota eliminada correctamente."
