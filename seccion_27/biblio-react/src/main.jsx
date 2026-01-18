// [MODIFICADO]
import React from 'react';
import ReactDOM from 'react-dom/client';

import { BrowserRouter } from "react-router-dom"; // [NUEVO]

import App from './App.jsx';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {/* [NUEVO] Envolver en router */}
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
