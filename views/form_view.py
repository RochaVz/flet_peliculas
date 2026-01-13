import flet as ft
from services.pelicula_service import crear, obtener_por_id, actualizar


def form_view(page: ft.Page, regresar_home, id_pelicula=None):
    # Configuración de página
    page.title = "Formulario de Película"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Limpiar vista anterior
    # page.controls.clear()

    pelicula = None
    if id_pelicula is not None:
        pelicula = obtener_por_id(id_pelicula)

    # ======================
    # CAMPOS DEL FORMULARIO
    # ======================

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

    # ======================
    # VALIDACIÓN
    # ======================

    def validar_formulario(e=None):
        valido = True

        # Título
        if not titulo_input.value.strip():
            titulo_input.error_text = "El título no puede estar vacío"
            valido = False
        else:
            titulo_input.error_text = None

        # Director
        if not director_input.value.strip():
            director_input.error_text = "El director no puede estar vacío"
            valido = False
        else:
            director_input.error_text = None

        # Puntuación
        valor = puntuacion_input.value.strip()
        if not valor:
            puntuacion_input.error_text = "Ingrese un número del 1 al 10"
            valido = False
        else:
            try:
                num = int(valor)
                if not (1 <= num <= 10):
                    puntuacion_input.error_text = "Debe ser un número entre 1 y 10"
                    valido = False
                else:
                    puntuacion_input.error_text = None
            except ValueError:
                puntuacion_input.error_text = "Debe ser un número entero"
                valido = False

        boton_guardar.disabled = not valido
        page.update()

    titulo_input.on_change = validar_formulario
    director_input.on_change = validar_formulario
    puntuacion_input.on_change = validar_formulario

    # ======================
    # GUARDAR
    # ======================

    def guardar_cambios(e=None):
        validar_formulario()

        if boton_guardar.disabled:
            return

        datos = {
            "titulo": titulo_input.value.strip(),
            "director": director_input.value.strip(),
            "puntuacion": int(puntuacion_input.value),
        }

        if pelicula:
            resultado = actualizar(pelicula.id, datos)
        else:
            resultado = crear(datos)

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

    # ======================
    # BOTONES (FLET CORRECTO)
    # ======================

    boton_guardar = ft.ElevatedButton(
        "Guardar Cambios" if pelicula else "Guardar",
        icon=ft.Icons.SAVE,
        on_click=guardar_cambios,
        disabled=True,
    )

    boton_cancelar = ft.ElevatedButton(
        "Cancelar",
        icon=ft.Icons.CANCEL,
        on_click=lambda e: regresar_home(),
        bgcolor=ft.Colors.RED_700,
    )

    botones = ft.Row(
        controls=[boton_guardar, boton_cancelar],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    # ======================
    # CONTENEDOR PRINCIPAL
    # ======================

    titulo_form = "Editar Película" if pelicula else "Agregar Nueva Película"

    formulario = ft.Container(
        width=500,
        content=ft.Column(
            controls=[
                ft.Text(titulo_form, size=26, weight=ft.FontWeight.BOLD),
                titulo_input,
                director_input,
                puntuacion_input,
                botones,
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    page.add(formulario)

    # Validación inicial
    validar_formulario()
