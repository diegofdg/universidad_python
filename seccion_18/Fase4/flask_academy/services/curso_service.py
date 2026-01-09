from extensions import db
from models import Curso

# ================================
# 🔍 Función para obtener todos los cursos
# ================================
def obtener_todos():
    """
    Retorna una lista con todos los cursos almacenados en la base de datos.
    """
    return Curso.query.all()
