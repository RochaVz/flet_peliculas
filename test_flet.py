import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Text(
            "Flet Web funciona ✅",
            size=30,
            color=ft.Colors.GREEN_400
        )
    )

ft.app(
    target=main,
    view=ft.AppView.WEB_BROWSER,
    port=8550
)
