import os
from flask import Flask, render_template, redirect, url_for, flash
from dotenv import load_dotenv
from extensions import db, migrate
from models import Curso
from services import curso_service
from forms import CursoForm

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

    @app.route("/")
    def index():
        cursos = curso_service.obtener_todos()
        return render_template("index.html", cursos=cursos)

    @app.route("/agregar", methods=["GET", "POST"])
    def agregar():
        form = CursoForm()
        if form.validate_on_submit():
            curso_service.agregar_curso(
                form.nombre.data,
                form.instructor.data,
                form.duracion.data
            )
            flash("✅ Curso agregado exitosamente", "success")
            return redirect(url_for("index"))
        return render_template("agregar_curso.html", form=form)

    @app.route("/editar/<int:id_curso>", methods=["GET", "POST"])
    def editar(id_curso):
        curso = curso_service.buscar_por_id(id_curso)
        if not curso:
            flash("⚠️ Curso no encontrado", "warning")
            return redirect(url_for("index"))

        form = CursoForm(obj=curso)
        if form.validate_on_submit():
            curso_service.editar_curso(
                id_curso,
                form.nombre.data,
                form.instructor.data,
                form.duracion.data
            )
            flash("✏️ Curso actualizado correctamente", "success")
            return redirect(url_for("index"))
        return render_template("editar_curso.html", form=form)

    # Nueva ruta para eliminar curso
    @app.route("/eliminar/<int:id_curso>")
    def eliminar(id_curso):
        curso = curso_service.buscar_por_id(id_curso)
        if not curso:
            flash("⚠️ Curso no encontrado", "warning")
        else:
            curso_service.eliminar_curso(id_curso)
            flash(f"🗑️ Curso '{curso.nombre}' eliminado exitosamente", "success")
        return redirect(url_for("index"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
