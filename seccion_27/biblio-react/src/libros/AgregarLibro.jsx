// [MODIFICADO]
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { crearLibro } from "../api/libros.js";

function AgregarLibro() {

  // [NUEVO] Estados del formulario
  const [titulo, setTitulo] = useState("");
  const [autor, setAutor] = useState("");
  const [rating, setRating] = useState("");

  const navigate = useNavigate(); // [NUEVO]

  // [NUEVO] manejar envío del formulario
  async function manejarSubmit(e) {
    e.preventDefault();

    try {
      const nuevoLibro = {
        titulo,
        autor,
        rating,
      };

      await crearLibro(nuevoLibro);

      alert("Libro creado correctamente");

      navigate("/"); // Redirigir al listado
    } catch (error) {
      alert(error.message || "Error al crear libro");
    }
  }

  return (
    <div className="col-12 col-md-8 col-lg-6 mx-auto">

      <h2 className="text-warning text-center mb-4">
        <i className="bi bi-book-half me-2"></i>
        Agregar Libro
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
          <button
            type="submit"
            className="btn btn-primary"
          >
            Guardar
          </button>

          <Link to="/" className="btn btn-secondary">
            Cancelar
          </Link>
        </div>
      </form>

    </div>
  );
}

export default AgregarLibro;
