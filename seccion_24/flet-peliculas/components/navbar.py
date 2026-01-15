import flet as ft


def navbar(on_home, on_add):
    return ft.Container(
        bgcolor=ft.Colors.BLUE_GREY_800,
        padding=15,
        content=ft.Row(
            controls=[
                ft.TextButton("Inicio", on_click=on_home),
                ft.TextButton("Agregar Película", on_click=on_add),
            ],
            alignment="center",
            spacing=50,
        ),
    )
