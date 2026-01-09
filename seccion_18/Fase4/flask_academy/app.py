import os
from flask import Flask, render_template
from dotenv import load_dotenv
from extensions import db, migrate
from models import Curso
from services import curso_service  # 👈 Importamos la capa de servicios

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-change-me")

    usuario = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    servidor = os.getenv("DB_HOST")
    puerto = os.getenv("DB_PORT")
    base_datos = os.getenv("DB_NAME")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{usuario}:{password}@{servidor}:{puerto}/{base_datos}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Ruta principal que lista los cursos
    @app.route("/")
    def index():
        cursos = curso_service.obtener_todos()
        return render_template("index.html", cursos=cursos)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
