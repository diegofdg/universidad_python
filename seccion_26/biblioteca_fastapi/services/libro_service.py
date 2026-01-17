# services/libro_service.py
# Capa de servicios encargada de la lógica relacionada con libros.

from sqlalchemy.orm import Session
from models.libro import Libro
from schemas import LibroCreate, LibroUpdate


def listar_libros(db: Session):
    """
    Devuelve una lista con todos los libros almacenados en la base de datos.
    """
    return db.query(Libro).all()


def crear_libro(db: Session, datos: LibroCreate):
    """
    Crea un nuevo libro en la base de datos usando los datos validados
    del esquema LibroCreate.
    """
    nuevo_libro = Libro(
        titulo=datos.titulo,
        autor=datos.autor,
        rating=datos.rating
    )
    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)
    return nuevo_libro


def obtener_libro_por_id(db: Session, id: int):
    """
    Obtiene un libro por su ID.
    Retorna el libro si existe; de lo contrario retorna None.
    """
    return db.query(Libro).filter(Libro.id == id).first()


def actualizar_libro(db: Session, id: int, datos: LibroUpdate):
    """
    Actualiza un libro existente.
    Solo se modifican los campos enviados.
    Retorna el libro actualizado o None si no existe.
    """
    libro = obtener_libro_por_id(db, id)
    if not libro:
        return None

    if datos.titulo is not None:
        libro.titulo = datos.titulo

    if datos.autor is not None:
        libro.autor = datos.autor

    if datos.rating is not None:
        libro.rating = datos.rating

    db.commit()
    db.refresh(libro)

    return libro


def eliminar_libro(db: Session, id: int):  # [NUEVO]
    """
    Elimina un libro de la base de datos si existe.       # [NUEVO]
    Retorna True si se eliminó, o None si no existe.     # [NUEVO]
    """                                                   # [NUEVO]

    libro = obtener_libro_por_id(db, id)                 # [NUEVO]
    if not libro:                                        # [NUEVO]
        return None                                      # [NUEVO]

    db.delete(libro)                                     # [NUEVO]
    db.commit()                                          # [NUEVO]

    return True                                          # [NUEVO]
