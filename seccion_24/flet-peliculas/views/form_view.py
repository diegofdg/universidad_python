import flet as ft
from services.pelicula_service import crear
from services.pelicula_service import obtener_por_id
from services.pelicula_service import actualizar


def form_view(page: ft.Page, regresar_home, id_pelicula=None):
    page.title = "Formulario de Película"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    pelicula = None

    if id_pelicula is not None:
        pelicula = obtener_por_id(id_pelicula)

    # Campos
    titulo_input = ft.TextField(
        label="Título",
        value=pelicula.titulo if pelicula else "",
        expand=True,
    )

    director_input = ft.TextField(
        label="Director",
        value=pelicula.director if pelicula else "",
        expand=True,
    )

    puntuacion_input = ft.TextField(
        label="Puntuación (1–10)",
        value=str(pelicula.puntuacion) if pelicula else "",
        expand=True,
    )

    # [NUEVO] error flags
    titulo_input.error_text = None
    director_input.error_text = None
    puntuacion_input.error_text = None

    # [NUEVO] función de validación dinámica
    def validar_formulario(e=None):
        valido = True

        # Validar título
        if not titulo_input.value.strip():
            titulo_input.error_text = "El título no puede estar vacío."
            valido = False
        else:
            titulo_input.error_text = None

        # Validar director
        if not director_input.value.strip():
            director_input.error_text = "El director no puede estar vacío."
            valido = False
        else:
            director_input.error_text = None

        # Validar puntuación
        valor = puntuacion_input.value.strip()

        if valor == "":
            puntuacion_input.error_text = "Ingrese un número del 1 al 10."
            valido = False
        else:
            try:
                num = int(valor)
                if not (1 <= num <= 10):
                    puntuacion_input.error_text = "Debe ser un número entre 1 y 10."
                    valido = False
                else:
                    puntuacion_input.error_text = None
            except:
                puntuacion_input.error_text = "Debe ser un número entero."
                valido = False

        boton_guardar.disabled = not valido
        page.update()

    # [NUEVO] conectar eventos
    titulo_input.on_change = validar_formulario
    director_input.on_change = validar_formulario
    puntuacion_input.on_change = validar_formulario

    # BOTÓN GUARDAR
    boton_guardar = ft.ElevatedButton(
        content=ft.Text("Guardar Cambios" if pelicula else "Guardar"),
        on_click=lambda e: guardar_cambios(),
        disabled=True  # [NUEVO]
    )

    # [MODIFICADO]
    def guardar_cambios():
        validar_formulario()

        if boton_guardar.disabled:
            return

        datos = {
            "titulo": titulo_input.value,
            "director": director_input.value,
            "puntuacion": puntuacion_input.value,
        }

        resultado = actualizar(pelicula.id, datos) if pelicula else crear(datos)

        if resultado["ok"]:
            page.snack_bar = ft.SnackBar(
                ft.Text(resultado["mensaje"]),
                bgcolor=ft.Colors.GREEN_700,
            )
            page.snack_bar.open = True
            page.update()
            regresar_home()
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text(resultado["mensaje"]),
                bgcolor=ft.Colors.RED_700,
            )
            page.snack_bar.open = True
            page.update()

    boton_cancelar = ft.ElevatedButton(
        content=ft.Text("Cancelar"),
        on_click=lambda e: regresar_home(),
        bgcolor=ft.Colors.RED_700,
    )

    botones = ft.Row(
        controls=[boton_guardar, boton_cancelar],
        alignment="center",
        spacing=20,
    )

    titulo_texto = "Editar Película" if pelicula else "Agregar Nueva Película"

    formulario = ft.Column(
        controls=[
            ft.Text(titulo_texto, size=26, weight=ft.FontWeight.BOLD),
            titulo_input,
            director_input,
            puntuacion_input,
            botones,
        ],
        spacing=20,
        alignment="center",
        horizontal_alignment="center",
        expand=True,
    )

    page.add(formulario)

    # [NUEVO] llamar validación inicial
    validar_formulario()
