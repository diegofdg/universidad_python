import { Link } from "react-router-dom";

function Navegacion() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark border-bottom border-secondary mb-4">
      <div className="container">
        
        <Link className="navbar-brand fw-bold text-warning" to="/">
          <i className="bi bi-book-half me-2"></i>
          Biblioteca Personal
        </Link>

        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ms-auto">

            {/* [NUEVO] Enlace hacia /agregar */}
            <li className="nav-item">
              <Link className="nav-link" to="/agregar">
                Agregar
              </Link>
            </li>

          </ul>
        </div>

      </div>
    </nav>
  );
}

export default Navegacion;
