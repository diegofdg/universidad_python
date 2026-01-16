# views/form_view.py (MODIFICADO)
# Se agrega botón "Eliminar" con confirmación simple.

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QFormLayout,
    QLineEdit, QPushButton, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt

from services.mascota_service import crear, obtener_por_id, actualizar, eliminar


class FormView(QWidget):
    """Formulario para agregar o editar una mascota."""

    def __init__(self, callback_cancelar=None, callback_refrescar=None):
        super().__init__()

        self.callback_cancelar = callback_cancelar
        self.callback_refrescar = callback_refrescar

        self.editando_id = None

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(40, 30, 40, 30)
        self.setLayout(layout)

        self.titulo = QLabel("Agregar Mascota")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet("font-size: 20pt; font-weight: bold;")

        self.subtitulo = QLabel("Complete la información de la mascota")
        self.subtitulo.setAlignment(Qt.AlignCenter)
        self.subtitulo.setStyleSheet("font-size: 12pt;")

        layout.addWidget(self.titulo)
        layout.addWidget(self.subtitulo)

        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignRight)

        self.input_nombre = QLineEdit()
        self.input_especie = QLineEdit()
        self.input_peso = QLineEdit()

        form_layout.addRow("Nombre:", self.input_nombre)
        form_layout.addRow("Especie:", self.input_especie)
        form_layout.addRow("Peso:", self.input_peso)

        layout.addLayout(form_layout)

        # Botones
        botones_layout = QHBoxLayout()

        self.btn_guardar = QPushButton("Guardar")
        self.btn_guardar.clicked.connect(self.guardar)

        self.btn_eliminar = QPushButton("Eliminar")   # [NUEVO]
        self.btn_eliminar.setVisible(False)           # solo en edición
        self.btn_eliminar.clicked.connect(self.eliminar_mascota)

        self.btn_cancelar = QPushButton("Cancelar")
        if self.callback_cancelar:
            self.btn_cancelar.clicked.connect(self.callback_cancelar)

        botones_layout.addWidget(self.btn_guardar)
        botones_layout.addWidget(self.btn_eliminar)
        botones_layout.addWidget(self.btn_cancelar)

        layout.addLayout(botones_layout)

    # --------------------------------------------------------
    def cargar_para_edicion(self, id_mascota):
        """Precargar el formulario para edición."""
        self.editando_id = id_mascota

        mascota = obtener_por_id(id_mascota)
        if not mascota:
            return

        self.input_nombre.setText(mascota.nombre)
        self.input_especie.setText(mascota.especie)
        self.input_peso.setText(str(mascota.peso))

        self.titulo.setText("Editar Mascota")
        self.subtitulo.setText("Modifique la información de la mascota")
        self.btn_guardar.setText("Guardar cambios")

        self.btn_eliminar.setVisible(True)    # <-- visible en edición

    # --------------------------------------------------------
    def guardar(self):
        """Guarda o actualiza según modo."""
        datos = {
            "nombre": self.input_nombre.text(),
            "especie": self.input_especie.text(),
            "peso": self.input_peso.text()
        }

        if self.editando_id is not None:
            ok, mensaje = actualizar(self.editando_id, datos)
        else:
            ok, mensaje = crear(datos)

        if not ok:
            QMessageBox.warning(self, "Error", mensaje)
            return

        QMessageBox.information(self, "Éxito", mensaje)

        if self.callback_refrescar:
            self.callback_refrescar()

        if self.callback_cancelar:
            self.callback_cancelar()

    # --------------------------------------------------------
    def eliminar_mascota(self):   # [NUEVO]
        """Confirmación y eliminación de mascota."""
        if self.editando_id is None:
            return

        confirmar = QMessageBox.question(
            self,
            "Confirmar eliminación",
            "¿Seguro que deseas eliminar esta mascota?",
        )

        if confirmar != QMessageBox.Yes:
            return

        ok, mensaje = eliminar(self.editando_id)

        if not ok:
            QMessageBox.warning(self, "Error", mensaje)
            return

        QMessageBox.information(self, "Éxito", mensaje)

        if self.callback_refrescar:
            self.callback_refrescar()

        if self.callback_cancelar:
            self.callback_cancelar()
