import flet as ft
from modules.calculatorApp import CalculatorApp

def main(page: ft.Page):
    """
    The main function that initializes and sets up the CalculatorApp on the given page.

    This function sets the title of the page, creates an instance of the CalculatorApp,
    and adds it to the page's control tree for display.

    Args:
        page (ft.Page): The Flet page object where the CalculatorApp will be rendered.
    """
    # Set the title of the calculator app page
    page.title = "Calculator App"
    
    # Create an instance of the CalculatorApp
    calc = CalculatorApp()

    # Add the calculator instance to the page for display
    page.add(calc)

# Start the Flet application with the main function as the target
ft.app(target=main)
