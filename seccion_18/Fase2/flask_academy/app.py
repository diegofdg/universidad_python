import os
from flask import Flask, render_template
from dotenv import load_dotenv
from extensions import db, migrate

# Carga variables de entorno desde .env
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Clave secreta para formularios y sesiones
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-change-me")

    # Configuración de conexión a MySQL
    usuario = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    servidor = os.getenv("DB_HOST")
    puerto = os.getenv("DB_PORT")
    base_datos = os.getenv("DB_NAME")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{usuario}:{password}@{servidor}:{puerto}/{base_datos}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inicializamos las extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Ruta principal
    @app.route("/")
    def index():
        return render_template("index.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
