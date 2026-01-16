# database.py (NUEVO)
# Maneja la conexión a MySQL usando SQLAlchemy y variables de entorno.

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

# -----------------------------
# Cargar variables desde .env
# -----------------------------
load_dotenv()

USER = os.getenv("DB_USER")
PASS = os.getenv("DB_PASS")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB   = os.getenv("DB_NAME")

# Construir URL de conexión
DATABASE_URL = f"mysql+pymysql://{USER}:{PASS}@{HOST}:{PORT}/{DB}"

# -----------------------------
# Configuración del motor SQLAlchemy
# -----------------------------
engine = create_engine(DATABASE_URL, echo=False, future=True)

# Session para operaciones ORM
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)

# Base para modelos ORM
Base = declarative_base()

# -----------------------------
# Prueba rápida de conexión
# -----------------------------
if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            print("✅ Conexión a MySQL exitosa:", connection)
    except SQLAlchemyError as e:
        print("❌ Error al conectar a MySQL:", str(e))
