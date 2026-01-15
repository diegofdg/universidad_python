import os
import pymysql
from dotenv import load_dotenv
import subprocess

load_dotenv()

# Datos de conexión
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


def limpiar_version_huerfana():
    """Elimina alembic_version si está dañada o huérfana"""
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            port=int(DB_PORT)
        )
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS alembic_version;")
        conn.commit()
        cursor.close()
        conn.close()
        print("✔ Tabla 'alembic_version' verificada/eliminada si era necesario.")
    except Exception as e:
        print("❌ Error limpiando alembic_version:", e)


def migrar():
    print("📌 Generando migración automática...")
    subprocess.run(["alembic", "revision", "--autogenerate", "-m", "auto"], check=False)

    print("📌 Aplicando migraciones...")
    subprocess.run(["alembic", "upgrade", "head"], check=False)


if __name__ == "__main__":
    print("🚀 Iniciando proceso de migración...")
    limpiar_version_huerfana()
    migrar()
    print("✅ Migración completada.")
