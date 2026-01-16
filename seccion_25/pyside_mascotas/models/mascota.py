# models/mascota.py (NUEVO)
# Modelo ORM que representa la tabla 'mascotas'

from sqlalchemy import Column, Integer, String, Float
from database import Base

class Mascota(Base):
    __tablename__ = "mascotas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    especie = Column(String(100), nullable=False)
    peso = Column(Float, nullable=True)

    def __repr__(self):
        return f"<Mascota id={self.id} nombre={self.nombre} especie={self.especie} peso={self.peso}>"
