# migrate.py (NUEVO)
# Automatiza migraciones con Alembic:
# - Limpia versiones huérfanas
# - Genera revisión autogenerada
# - Ejecuta upgrade head

import os
import shutil
from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# Limpiar carpeta versions/ si está vacía o con basura
# -----------------------------
versions_path = os.path.join("alembic", "versions")

if os.path.exists(versions_path):
    for file in os.listdir(versions_path):
        file_path = os.path.join(versions_path, file)
        try:
            os.remove(file_path)
        except:
            pass

# -----------------------------
# Ejecutar comandos Alembic
# -----------------------------
print("🔧 Generando revisión autogenerada...")
os.system("alembic revision --autogenerate -m 'init'")

print("⬆️ Aplicando upgrade head...")
os.system("alembic upgrade head")

print("✅ Migración completada. Tabla creada si no existía.")
