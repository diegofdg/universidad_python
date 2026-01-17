# main.py
# Punto de entrada de la aplicación FastAPI.

from fastapi import FastAPI
from api.libros import router as libros_router
from fastapi.middleware.cors import CORSMiddleware  # [NUEVO]

app = FastAPI(
    title="API Biblioteca Personal",
    description="Backend REST con FastAPI y MySQL para administrar libros personales.",
    version="1.0.0"
)

# -----------------------------------------------------------
# Configuración de CORS                                      # [NUEVO]
# -----------------------------------------------------------
origins = [                                                # [NUEVO]
    "http://localhost:4200",  # Angular                    # [NUEVO]
    "http://localhost:5173",  # React Vite                 # [NUEVO]
]                                                           # [NUEVO]

app.add_middleware(                                        # [NUEVO]
    CORSMiddleware,                                        # [NUEVO]
    allow_origins=origins,                                 # [NUEVO]
    allow_credentials=True,                                # [NUEVO]
    allow_methods=["*"],                                    # [NUEVO]
    allow_headers=["*"],                                    # [NUEVO]
)

# -----------------------------------------------------------
# Endpoint de prueba inicial
# -----------------------------------------------------------
@app.get("/")
def home():
    """
    Endpoint inicial para verificar que la API está funcionando.
    """
    return {"mensaje": "API de Biblioteca funcionando correctamente"}

# -----------------------------------------------------------
# Incluir router de libros
# -----------------------------------------------------------
app.include_router(libros_router)
