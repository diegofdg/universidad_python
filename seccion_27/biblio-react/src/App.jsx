// [MODIFICADO]
import { Routes, Route } from "react-router-dom";

import Navegacion from "./componentes/Navegacion.jsx";
import ListadoLibros from "./libros/ListadoLibros.jsx";
import AgregarLibro from "./libros/AgregarLibro.jsx";
import EditarLibro from "./libros/EditarLibro.jsx"; // [NUEVO]

function App() {
  return (
    <main className="container pt-4">

      <Navegacion />

      <Routes>
        <Route path="/" element={<ListadoLibros />} />
        <Route path="/agregar" element={<AgregarLibro />} />
        <Route path="/editar/:id" element={<EditarLibro />} /> {/* [NUEVO] */}
      </Routes>

    </main>
  );
}

export default App;
