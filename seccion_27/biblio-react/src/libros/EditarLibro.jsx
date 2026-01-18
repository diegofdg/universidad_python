// [MODIFICADO]
import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { obtenerLibroPorId, actualizarLibro } from "../api/libros.js";

function EditarLibro() {

  const { id } = useParams();
  const navigate = useNavigate(); // [NUEVO]

  const [titulo, setTitulo] = useState("");
  const [autor, setAutor] = useState("");
  const [rating, setRating] = useState("");

  // [EXISTENTE] Precargar datos
  useEffect(() => {
    async function cargarLibro() {
      try {
        const libro = await obtenerLibroPorId(id);
        setTitulo(libro.titulo);
        setAutor(libro.autor);
        setRating(libro.rating);
      } catch (error) {
        alert("Error al cargar los datos del libro");
      }
    }
    cargarLibro();
  }, [id]);

  // [NUEVO] Guardar cambios
  async function manejarSubmit(e) {
    e.preventDefault();

    try {
      const libroActualizado = {
        titulo,
        autor,
        rating
      };

      await actualizarLibro(id, libroActualizado);

      alert("Libro actualizado correctamente");

      navigate("/"); // regresar al listado
    } catch (error) {
      alert(error.message || "Error al actualizar libro");
    }
  }

  return (
    <div className="col-12 col-md-8 col-lg-6 mx-auto">

      <h2 className="text-warning text-center mb-4">
        <i className="bi bi-book-half me-2"></i>
        Editar Libro
      </h2>

      <form onSubmit={manejarSubmit}>
        <div className="mb-3">
          <label className="form-label text-light">Título</label>
          <input
            type="text"
            className="form-control"
            value={titulo}
            onChange={(e) => setTitulo(e.target.value)}
          />
        </div>

        <div className="mb-3">
          <label className="form-label text-light">Autor</label>
          <input
            type="text"
            className="form-control"
            value={autor}
            onChange={(e) => setAutor(e.target.value)}
          />
        </div>

        <div className="mb-3">
          <label className="form-label text-light">Rating (1-5)</label>
          <input
            type="number"
            className="form-control"
            min="1"
            max="5"
            value={rating}
            onChange={(e) => setRating(e.target.value)}
          />
        </div>

        <div className="d-flex gap-2">
          <button type="submit" className="btn btn-primary">
            Guardar Cambios
          </button>

          <Link to="/" className="btn btn-secondary">
            Cancelar
          </Link>
        </div>

      </form>

    </div>
  );
}

export default EditarLibro;
