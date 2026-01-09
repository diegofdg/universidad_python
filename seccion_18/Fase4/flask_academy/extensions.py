from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inicializamos las extensiones de forma global
db = SQLAlchemy()
migrate = Migrate()
