import flet as ft
from styles.style_buttons import (
    DigitButton,
    ActionButton,
    ExtraActionButton,
)


def main(page: ft.Page):
    page.title = "Calc App"

    result = ft.Text(value="0", color=ft.colors.WHITE, size=20)

    page.add(
        ft.Container(
            width=350,
            bgcolor=ft.colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[result], alignment="end"),
                    ft.Row(
                        controls=[
                            ExtraActionButton(text="AC"),
                            ExtraActionButton(text="+/-"),
                            ExtraActionButton(text="%"),
                            ActionButton(text="/"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="7"),
                            DigitButton(text="8"),
                            DigitButton(text="9"),
                            ActionButton(text="*"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="4"),
                            DigitButton(text="5"),
                            DigitButton(text="6"),
                            ActionButton(text="-"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="1"),
                            DigitButton(text="2"),
                            DigitButton(text="3"),
                            ActionButton(text="+"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="0", expand=2),
                            DigitButton(text="."),
                            ActionButton(text="="),
                        ]
                    ),
                ]
            ),
        )
    )


if __name__ == "__main__":
    ft.app(main)
