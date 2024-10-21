import flet as ft

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand


class DigitButton(CalcButton):
    def __init__(self, text, expand=1):
        CalcButton.__init__(self, text, expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE


class ActionButton(CalcButton):
    def __init__(self, text):
        CalcButton.__init__(self, text)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE


class ExtraActionButton(CalcButton):
    def __init__(self, text):
        CalcButton.__init__(self, text)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK
