from extensions import db
from models import Curso

def obtener_todos():
    return Curso.query.all()

# ================================
# 🧩 Función para agregar un curso nuevo
# ================================
def agregar_curso(nombre, instructor, duracion):
    """
    Crea un nuevo curso en la base de datos.
    """
    nuevo_curso = Curso(nombre=nombre, instructor=instructor, duracion=duracion)
    db.session.add(nuevo_curso)
    db.session.commit()
