from extensions import db

# Clase que representa la tabla 'curso' en la base de datos
class Curso(db.Model):
    __tablename__ = "curso"

    id_curso = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    instructor = db.Column(db.String(100), nullable=False)
    duracion = db.Column(db.Numeric(5, 2), nullable=False)

    def __repr__(self):
        return f"<Curso {self.nombre}>"
