import flet as ft


def dialogo_confirmacion(mensaje, on_confirmar, on_cancelar):
    return ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirmar acción"),
        content=ft.Text(mensaje),
        actions=[
            ft.TextButton("Cancelar", on_click=on_cancelar),
            ft.TextButton("Eliminar", on_click=on_confirmar),
        ],
        actions_alignment="end",
    )
