import flet as ft
import socket

from views.home_view import home_view
from components.navbar import navbar
from views.form_view import form_view
from components.dialogs import dialogo_confirmacion
from services.pelicula_service import eliminar


# [NUEVO]
def get_local_ip():
    """Obtiene la IP local real de la computadora."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"


def main(page: ft.Page):

    # [NUEVO]
    def ir_eliminar(id_pelicula):
        def confirmar(e):
            resultado = eliminar(id_pelicula)

            page.dialog.open = False
            page.update()

            if resultado["ok"]:
                page.snack_bar = ft.SnackBar(
                    ft.Text(resultado["mensaje"]),
                    bgcolor=ft.Colors.GREEN_700,
                )
                page.snack_bar.open = True
                page.update()

                ir_home()
            else:
                page.snack_bar = ft.SnackBar(
                    ft.Text(resultado["mensaje"]),
                    bgcolor=ft.Colors.RED_700,
                )
                page.snack_bar.open = True
                page.update()

        def cancelar(e):
            page.dialog.open = False
            page.update()

        page.dialog = dialogo_confirmacion(
            "¿Seguro que deseas eliminar esta película?",
            confirmar,
            cancelar
        )

        page.overlay.append(page.dialog)
        page.dialog.open = True
        page.update()

    def ir_editar(id_pelicula):
        page.controls.clear()
        page.add(navbar(ir_home, ir_add))
        form_view(page, ir_home, id_pelicula)
        page.update()

    def ir_home(e=None):
        page.controls.clear()
        page.add(navbar(ir_home, ir_add))
        home_view(page, ir_editar, ir_eliminar)
        page.update()

    def ir_add(e=None):
        page.controls.clear()
        page.add(navbar(ir_home, ir_add))
        form_view(page, ir_home)
        page.update()

    page.add(navbar(ir_home, ir_add))
    home_view(page, ir_editar, ir_eliminar)


if __name__ == "__main__":
    ip_local = get_local_ip()

    print("===================================================")
    print("🚀 Servidor Flet ejecutándose…")
    print("📌 Accede desde este navegador:")
    print(f"   👉 http://localhost:8550")
    print(f"   👉 http://{ip_local}:8550 (otros dispositivos)")
    print("===================================================")

    ft.run(
        main,                       # 👈 así
        host="0.0.0.0",
        port=8550,
        view=ft.AppView.WEB_BROWSER
    )
