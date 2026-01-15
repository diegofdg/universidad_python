import flet as ft
from services.pelicula_service import obtener_todos


# [MODIFICADO]
def home_view(page: ft.Page, ir_editar, ir_eliminar):
    page.title = "🎞️ Flet Películas"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    peliculas = obtener_todos()
    filas = []

    for p in peliculas:
        filas.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(p.id))),
                    ft.DataCell(ft.Text(p.titulo)),
                    ft.DataCell(ft.Text(p.director)),
                    ft.DataCell(ft.Text(str(p.puntuacion))),
                    ft.DataCell(
                        ft.Row(
                            controls=[
                                # EDITAR
                                ft.IconButton(
                                    icon=ft.Icons.EDIT,
                                    tooltip="Editar",
                                    on_click=lambda e, id=p.id: ir_editar(id)
                                ),
                                # [NUEVO] ELIMINAR
                                ft.IconButton(
                                    icon=ft.Icons.DELETE,
                                    icon_color=ft.Colors.RED_400,
                                    tooltip="Eliminar",
                                    on_click=lambda e, id=p.id: ir_eliminar(id)
                                ),
                            ],
                            spacing=10
                        )
                    ),
                ]
            )
        )

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Título")),
            ft.DataColumn(ft.Text("Director")),
            ft.DataColumn(ft.Text("Puntuación")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=filas,
    )

    titulo_fila = ft.Row(
        controls=[
            ft.Icon(ft.Icons.MOVIE, size=40),
            ft.Text("Flet Películas", size=30, weight=ft.FontWeight.BOLD),
        ],
        alignment="center",
    )

    subtitulo = ft.Text("Listado de películas", size=18)

    contenido = ft.Column(
        controls=[titulo_fila, subtitulo, tabla],
        alignment="center",
        horizontal_alignment="center",
        spacing=20,
        expand=True,
    )

    page.add(contenido)
