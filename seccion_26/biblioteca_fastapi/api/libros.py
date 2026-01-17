# api/libros.py
# Router encargado de exponer las rutas relacionadas con libros.

from fastapi import APIRouter, Depends, HTTPException, Path
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from services.libro_service import (
    listar_libros,
    crear_libro,
    obtener_libro_por_id,
    actualizar_libro,
    eliminar_libro,     # [NUEVO]
)
from schemas import LibroRead, LibroCreate, LibroUpdate

# Crear router con prefijo y etiqueta
router = APIRouter(
    prefix="/api/libros",
    tags=["Libros"]
)

# GET /api/libros  (listar)
@router.get("/", response_model=List[LibroRead])
def obtener_libros(db: Session = Depends(get_db)):
    """
    Devuelve la lista completa de libros usando la capa de servicios.
    """
    return listar_libros(db)


# POST /api/libros  (crear)
@router.post("/", response_model=LibroRead, status_code=201)
def crear_libro_endpoint(datos: LibroCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo libro en la base de datos.
    """
    return crear_libro(db, datos)


# GET /api/libros/{id}
@router.get("/{id}", response_model=LibroRead)
def obtener_libro_endpoint(
    id: int = Path(..., gt=0, description="ID del libro a consultar"),
    db: Session = Depends(get_db)
):
    """
    Devuelve un libro específico según su ID.
    """
    libro = obtener_libro_por_id(db, id)
    if not libro:
        raise HTTPException(
            status_code=404,
            detail=f"Libro con id {id} no encontrado"
        )
    return libro


# PUT /api/libros/{id}
@router.put(
    "/{id}",
    response_model=LibroRead,
    status_code=200
)
def actualizar_libro_endpoint(
    id: int = Path(..., gt=0, description="ID del libro a actualizar"),
    datos: LibroUpdate = None,
    db: Session = Depends(get_db)
):
    """
    Actualiza un libro existente.
    """
    libro_actualizado = actualizar_libro(db, id, datos)

    if not libro_actualizado:
        raise HTTPException(
            status_code=404,
            detail=f"Libro con id {id} no encontrado"
        )
    return libro_actualizado


# DELETE /api/libros/{id}  -------------------------------------------- [NUEVO]
@router.delete(
    "/{id}",
    status_code=204
)  # [NUEVO]
def eliminar_libro_endpoint(
    id: int = Path(..., gt=0, description="ID del libro a eliminar"),  # [NUEVO]
    db: Session = Depends(get_db)                                      # [NUEVO]
):  # [NUEVO]
    """
    Elimina un libro por su ID.                                       # [NUEVO]
    Devuelve 204 si se eliminó, o 404 si no existe.                   # [NUEVO]
    """                                                               # [NUEVO]

    resultado = eliminar_libro(db, id)                                # [NUEVO]

    if not resultado:                                                 # [NUEVO]
        raise HTTPException(                                          # [NUEVO]
            status_code=404,
            detail=f"Libro con id {id} no encontrado"
        )
    return None                                                       # [NUEVO]
