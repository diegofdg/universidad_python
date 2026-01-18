// [MODIFICADO]
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { listarLibros, eliminarLibro } from "../api/libros.js"; // [NUEVO]

function ListadoLibros() {

  const [libros, setLibros] = useState([]);

  // [EXISTENTE] Cargar libros
  async function cargarDatos() {
    try {
      const data = await listarLibros();
      setLibros(data);
    } catch (error) {
      alert("Error al cargar los libros");
    }
  }

  useEffect(() => {
    cargarDatos();
  }, []);

  // [NUEVO] Eliminar libro
  async function borrar(id) {
    const confirmar = confirm("¿Seguro que deseas eliminar este libro?");
    if (!confirmar) return;

    try {
      await eliminarLibro(id);
      alert("Libro eliminado correctamente");
      cargarDatos(); // refresca la tabla
    } catch (error) {
      alert(error.message || "Error al eliminar libro");
    }
  }

  return (
    <div className="col-12 col-md-10 col-lg-8 mx-auto">

      <h2 className="text-warning text-center mb-4">
        <i className="bi bi-book-half me-2"></i>
        Listado de Libros
      </h2>

      <p className="text-light text-center">
        Aquí podrás visualizar todos los libros registrados en el sistema.
      </p>

      <div className="table-responsive">
        <table className="table table-dark table-striped table-hover">
          <thead className="table-primary">
            <tr>
              <th>ID</th>
              <th>Título</th>
              <th>Autor</th>
              <th>Rating</th>
              <th>Acciones</th> 
            </tr>
          </thead>
          <tbody>
            {libros.map((libro) => (
              <tr key={libro.id}>
                <td>{libro.id}</td>
                <td>{libro.titulo}</td>
                <td>{libro.autor}</td>
                <td>{libro.rating}</td>

                <td className="d-flex gap-2">

                  {/* Botón Editar */}
                  <Link
                    to={`/editar/${libro.id}`}
                    className="btn btn-sm btn-outline-primary"
                  >
                    <i className="bi bi-pencil-square me-1"></i>
                    Editar
                  </Link>

                  {/* [NUEVO] Botón Eliminar */}
                  <button
                    onClick={() => borrar(libro.id)}
                    className="btn btn-sm btn-outline-danger"
                  >
                    <i className="bi bi-trash me-1"></i>
                    Eliminar
                  </button>

                </td>

              </tr>
            ))}
          </tbody>
        </table>
      </div>

    </div>
  );
}

export default ListadoLibros;
