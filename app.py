import flet as ft
from views.home_view import home_view
from components.navbar import navbar
from views.form_view import form_view
from components.dialogs import dialogo_confirmacion
from services.pelicula_service import eliminar


def main(page: ft.Page):

    def ir_eliminar(id_pelicula):
        def confirmar(e):
            resultado = eliminar(id_pelicula)
            page.dialog.open = False
            page.update()
            ir_home()

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

    def ir_home(e=None):
        page.controls.clear()
        page.add(navbar(ir_home, ir_add))
        home_view(page, ir_editar, ir_eliminar)

    def ir_add(e=None):
        page.controls.clear()
        page.add(navbar(ir_home, ir_add))
        form_view(page, ir_home)

    page.add(navbar(ir_home, ir_add))
    home_view(page, ir_editar, ir_eliminar)


if __name__ == "__main__":
    ft.run(
        main,
        view=ft.AppView.FLET_APP
    )
