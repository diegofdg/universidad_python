from sqlalchemy import Column, Integer, String
from database import Base


class Pelicula(Base):
    __tablename__ = "peliculas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    director = Column(String(255), nullable=False)
    puntuacion = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Pelicula(id={self.id}, titulo='{self.titulo}', director='{self.director}', puntuacion={self.puntuacion})"
