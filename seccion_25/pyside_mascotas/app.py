# app.py
# Ventana principal con navegación y callbacks completos (hasta Fase 13)

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PySide6.QtGui import QAction
import qdarkstyle

from views.home_view import HomeView
from views.form_view import FormView


class MainWindow(QMainWindow):
    """Ventana principal con navegación entre vistas y soporte para agregar/editar."""

    def __init__(self):
        super().__init__()

        # -------------------------
        # Configuración de ventana
        # -------------------------
        self.setWindowTitle("🐾 PySide Mascotas")
        self.resize(1280, 720)

        # -------------------------
        # Contenedor de vistas
        # -------------------------
        self.stacked = QStackedWidget()

        # HomeView obtiene callback para editar (doble clic)
        self.home_view = HomeView(callback_editar=self.editar_mascota)

        # FormView obtiene callbacks para cancelar y refrescar
        self.form_view = FormView(
            callback_cancelar=self.ir_a_inicio,
            callback_refrescar=self.refrescar_home
        )

        # Agregar vistas al StackedWidget
        self.stacked.addWidget(self.home_view)   # index 0
        self.stacked.addWidget(self.form_view)   # index 1

        self.setCentralWidget(self.stacked)

        # -------------------------
        # Barra de herramientas
        # -------------------------
        toolbar = self.addToolBar("Navegación")

        accion_inicio = QAction("Inicio", self)
        accion_agregar = QAction("Agregar Mascota", self)

        toolbar.addAction(accion_inicio)
        toolbar.addAction(accion_agregar)

        accion_inicio.triggered.connect(self.ir_a_inicio)
        accion_agregar.triggered.connect(self.ir_a_formulario)

    # ========================================
    # NAVEGACIÓN
    # ========================================

    def ir_a_inicio(self):
        """Regresa al listado (HomeView)."""
        self.stacked.setCurrentIndex(0)

    def ir_a_formulario(self):
        """Muestra el formulario en modo 'Agregar Mascota'."""

        # Reset al modo de agregar
        self.form_view.editando_id = None

        # Restaurar textos de encabezado
        self.form_view.titulo.setText("Agregar Mascota")
        self.form_view.subtitulo.setText("Complete la información de la mascota")
        self.form_view.btn_guardar.setText("Guardar")

        # Limpiar entradas
        self.form_view.input_nombre.clear()
        self.form_view.input_especie.clear()
        self.form_view.input_peso.clear()

        self.stacked.setCurrentIndex(1)

    def refrescar_home(self):
        """Refresca la tabla del listado."""
        self.home_view.cargar_tabla()

    # ========================================
    # EDICIÓN (invocado por doble clic)
    # ========================================

    def editar_mascota(self, id_mascota):
        """Pasa el ID al formulario para precarga y navega a la vista de edición."""

        # Formulario entra en modo edición
        self.form_view.cargar_para_edicion(id_mascota)

        # Cambiar vista al formulario
        self.stacked.setCurrentIndex(1)


# ========================================
# FUNCIÓN MAIN
# ========================================

def main():
    app = QApplication(sys.argv)

    # Activar modo oscuro
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    ventana = MainWindow()
    ventana.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
