import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Navegacion from './Navegacion.jsx'
import ListadoEmpleados from './empleados/ListadoEmpleados.jsx'
import AgregarEmpleado from './empleados/AgregarEmpleado.jsx'
import EditarEmpleado from './empleados/EditarEmpleado.jsx'

export default function App() {
  return (
    <BrowserRouter>
      <Navegacion />
      <div className="container pb-4">
        <Routes>
          <Route path="/" element={<ListadoEmpleados />} />
          <Route path="/agregar" element={<AgregarEmpleado />} />
          <Route path="/editar/:idEmpleado" element={<EditarEmpleado />} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}
