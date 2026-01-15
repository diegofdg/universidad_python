from database import Session
from models.pelicula import Pelicula


def obtener_todos():
    session = Session()
    peliculas = session.query(Pelicula).all()
    session.close()
    return peliculas


def obtener_por_id(id):
    session = Session()
    pelicula = session.query(Pelicula).filter_by(id=id).first()
    session.close()
    return pelicula


def crear(datos):
    titulo = datos.get("titulo", "").strip()
    director = datos.get("director", "").strip()
    puntuacion = datos.get("puntuacion")

    # [MODIFICADO] Validaciones más descriptivas
    if not titulo:
        return {"ok": False, "mensaje": "El título no puede estar vacío."}

    if not director:
        return {"ok": False, "mensaje": "El director no puede estar vacío."}

    try:
        puntuacion = int(puntuacion)
    except Exception:
        return {"ok": False, "mensaje": "La puntuación debe ser un número entero."}

    if puntuacion < 1 or puntuacion > 10:
        return {"ok": False, "mensaje": "La puntuación debe estar entre 1 y 10."}

    session = Session()

    nueva = Pelicula(
        titulo=titulo,
        director=director,
        puntuacion=puntuacion
    )

    session.add(nueva)
    session.commit()
    session.close()

    return {"ok": True, "mensaje": "Película registrada correctamente."}


def actualizar(id, datos):
    session = Session()
    pelicula = session.query(Pelicula).filter_by(id=id).first()

    if not pelicula:
        session.close()
        return {"ok": False, "mensaje": "La película no existe."}

    titulo = datos.get("titulo", "").strip()
    director = datos.get("director", "").strip()
    puntuacion = datos.get("puntuacion", "").strip()

    # [MODIFICADO] Validaciones mejoradas
    if not titulo:
        session.close()
        return {"ok": False, "mensaje": "El título no puede estar vacío."}

    if not director:
        session.close()
        return {"ok": False, "mensaje": "El director no puede estar vacío."}

    try:
        puntuacion = int(puntuacion)
    except Exception:
        session.close()
        return {"ok": False, "mensaje": "La puntuación debe ser un número entero."}

    if puntuacion < 1 or puntuacion > 10:
        session.close()
        return {"ok": False, "mensaje": "La puntuación debe estar entre 1 y 10."}

    # [NUEVO]
    pelicula.titulo = titulo
    pelicula.director = director
    pelicula.puntuacion = puntuacion

    session.commit()
    session.close()

    return {"ok": True, "mensaje": "Película actualizada correctamente."}


# [NUEVO]
def eliminar(id):
    """Elimina una película por su ID."""
    session = Session()
    pelicula = session.query(Pelicula).filter_by(id=id).first()

    if not pelicula:
        session.close()
        return {"ok": False, "mensaje": "La película no existe."}

    session.delete(pelicula)
    session.commit()
    session.close()

    return {"ok": True, "mensaje": "Película eliminada correctamente."}


# PRUEBAS RÁPIDAS OPCIONALES
if __name__ == "__main__":
    print("=== Pruebas rápidas del servicio ===")

    print("→ Obtener película con ID 1:")
    prueba = obtener_por_id(1)
    if prueba:
        print("   ✔ Encontrada:", prueba)
    else:
        print("   ✘ No existe")

    print("\n→ Listado actual de películas:")
    for p in obtener_todos():
        print("  -", p)
