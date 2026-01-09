from extensions import db
from models import Curso

def obtener_todos():
    return Curso.query.all()

def agregar_curso(nombre, instructor, duracion):
    nuevo_curso = Curso(nombre=nombre, instructor=instructor, duracion=duracion)
    db.session.add(nuevo_curso)
    db.session.commit()

# ================================
# 🔍 Buscar curso por ID
# ================================
def buscar_por_id(id_curso):
    return Curso.query.get(id_curso)

# ================================
# ✏️ Editar curso existente
# ================================
def editar_curso(id_curso, nombre, instructor, duracion):
    curso = Curso.query.get(id_curso)
    if curso:
        curso.nombre = nombre
        curso.instructor = instructor
        curso.duracion = duracion
        db.session.commit()
