# views/home_view.py (MODIFICADO)
# Se agrega detección por doble clic en la tabla para obtener el ID.

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QSizePolicy, QTableView,
    QHeaderView, QMessageBox
)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

from services.mascota_service import obtener_todos


class HomeView(QWidget):
    """Vista principal tipo dashboard que lista mascotas."""

    def __init__(self, callback_editar=None):
        super().__init__()

        self.callback_editar = callback_editar  # se usará en Fase 13

        # --- Layout principal ---
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(30, 20, 30, 20)
        self.setLayout(layout)

        # --- Título ---
        titulo = QLabel("Sistema de Adopción de Mascotas")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 20pt; font-weight: bold;")
        titulo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # --- Subtítulo ---
        subtitulo = QLabel("Listado de Mascotas Registradas")
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setStyleSheet("font-size: 12pt;")
        subtitulo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout.addWidget(titulo)
        layout.addWidget(subtitulo)

        # --- Tabla ---
        self.tabla = QTableView()
        self.tabla.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tabla.setStyleSheet("""
            QTableView {
                border: none;
                gridline-color: #444;
                font-size: 11pt;
            }
        """)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setEditTriggers(QTableView.NoEditTriggers)  # Solo lectura

        # Conectar doble clic
        self.tabla.doubleClicked.connect(self.on_double_click)

        layout.addWidget(self.tabla)

        # Cargar datos
        self.cargar_tabla()

    # -----------------------------------------
    def cargar_tabla(self):
        """Carga los registros en el QTableView."""
        mascotas = obtener_todos()

        modelo = QStandardItemModel()
        modelo.setHorizontalHeaderLabels(["ID", "Nombre", "Especie", "Peso (kg)"])

        for m in mascotas:
            fila = [
                QStandardItem(str(m.id)),
                QStandardItem(m.nombre),
                QStandardItem(m.especie),
                QStandardItem(str(m.peso)),
            ]
            modelo.appendRow(fila)

        self.tabla.setModel(modelo)

        header = self.tabla.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.tabla.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    # -----------------------------------------
    def on_double_click(self, index):  # [NUEVO]
        """Detecta doble clic en una fila y muestra el ID seleccionado."""
        fila = index.row()
        id_item = self.tabla.model().item(fila, 0)  # Columna 0 → ID
        id_mascota = id_item.text()

        # Fase 11: mostrar ID en un mensaje
        QMessageBox.information(self, "Editar mascota",
                                f"ID seleccionado para editar: {id_mascota}")

        # Guardamos callback para fase posterior (13)
        if self.callback_editar:
            self.callback_editar(id_mascota)
