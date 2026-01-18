import axios from "axios";

const urlBase = "http://localhost:8000/api/libros";

const api = axios.create({
  baseURL: urlBase,
});

// [EXISTENTE]
async function listarLibros() {
  try {
    const respuesta = await api.get("/");
    return respuesta.data;
  } catch (error) {
    console.error("Error al listar libros:", error);
    throw error;
  }
}

// [EXISTENTE]
async function crearLibro(libro) {
  if (!libro.titulo || libro.titulo.trim() === "") {
    throw new Error("El título es obligatorio");
  }

  if (!libro.autor || libro.autor.trim() === "") {
    throw new Error("El autor es obligatorio");
  }

  const rating = Number(libro.rating);
  if (isNaN(rating) || rating < 1 || rating > 5) {
    throw new Error("El rating debe ser un número entre 1 y 5");
  }

  try {
    const respuesta = await api.post("/", libro);
    return respuesta.data;
  } catch (error) {
    console.error("Error al crear libro:", error);
    throw error;
  }
}

// [EXISTENTE]
async function obtenerLibroPorId(id) {
  try {
    const respuesta = await api.get(`/${id}`);
    return respuesta.data;
  } catch (error) {
    console.error(`Error al obtener libro con id ${id}:`, error);
    throw new Error("No se pudo obtener el libro solicitado");
  }
}

// [EXISTENTE]
async function actualizarLibro(id, libro) {
  if (!libro.titulo || libro.titulo.trim() === "") {
    throw new Error("El título es obligatorio");
  }

  if (!libro.autor || libro.autor.trim() === "") {
    throw new Error("El autor es obligatorio");
  }

  const rating = Number(libro.rating);
  if (isNaN(rating) || rating < 1 || rating > 5) {
    throw new Error("El rating debe ser un número entre 1 y 5");
  }

  try {
    const respuesta = await api.put(`/${id}`, libro);
    return respuesta.data;
  } catch (error) {
    console.error(`Error al actualizar libro con id ${id}:`, error);
    throw new Error("No se pudo actualizar el libro");
  }
}

// [NUEVO]
async function eliminarLibro(id) {
  try {
    const respuesta = await api.delete(`/${id}`);
    return respuesta.data;
  } catch (error) {
    console.error(`Error al eliminar libro con id ${id}:`, error);
    throw new Error("No se pudo eliminar el libro");
  }
}

export {
  api,
  urlBase,
  listarLibros,
  crearLibro,
  obtenerLibroPorId,
  actualizarLibro,
  eliminarLibro   // [NUEVO]
};
