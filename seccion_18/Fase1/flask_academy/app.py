import os
from flask import Flask, render_template
from dotenv import load_dotenv

# Carga variables de entorno desde .env (para usar SECRET_KEY ahora
# y más tarde las credenciales de la base de datos).
load_dotenv()

# Patron de diseño Application Factory
def create_app():
    app = Flask(__name__)

    # SECRET_KEY se usa para sesiones y protección CSRF (lo necesitaremos con Flask-WTF).
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-change-me")

    # Ruta principal (aún sin lógica de negocio; solo renderiza la plantilla base).
    @app.route("/")
    def index():
        return render_template("index.html")

    return app


# Soporte para ejecutar en PyCharm con botón "Run"
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
