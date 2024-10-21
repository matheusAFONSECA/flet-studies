import flet as ft
from styles.style_buttons import DigitButton, ActionButton, ExtraActionButton


class CalculatorApp(ft.Container):
    """
    A class representing a simple calculator application using Flet.
    
    This class is responsible for creating the user interface of the calculator and handling
    the logic for basic arithmetic operations like addition, subtraction, multiplication, division,
    and other functions like percentage, negation, and resetting the calculator.
    """
    def __init__(self):
        """
        Initializes the CalculatorApp instance, setting up the UI components, result display,
        and the default state of the calculator.
        """
        super().__init__()
        self.reset()  # Reset the calculator to its initial state

        # Create the result display text field
        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=20)
        
        # Define container properties
        self.width = 350
        self.bgcolor = ft.colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20

        # Define the layout of the calculator using rows and buttons
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.result], alignment="end"),  # Display result on top
                
                # First row of buttons (AC, +/- , %, /)
                ft.Row(
                    controls=[
                        ExtraActionButton(
                            text="AC", button_clicked=self.button_clicked
                        ),
                        ExtraActionButton(
                            text="+/-", button_clicked=self.button_clicked
                        ),
                        ExtraActionButton(text="%", button_clicked=self.button_clicked),
                        ActionButton(text="/", button_clicked=self.button_clicked),
                    ]
                ),
                
                # Second row of digit buttons (7, 8, 9, *)
                ft.Row(
                    controls=[
                        DigitButton(text="7", button_clicked=self.button_clicked),
                        DigitButton(text="8", button_clicked=self.button_clicked),
                        DigitButton(text="9", button_clicked=self.button_clicked),
                        ActionButton(text="*", button_clicked=self.button_clicked),
                    ]
                ),
                
                # Third row of digit buttons (4, 5, 6, -)
                ft.Row(
                    controls=[
                        DigitButton(text="4", button_clicked=self.button_clicked),
                        DigitButton(text="5", button_clicked=self.button_clicked),
                        DigitButton(text="6", button_clicked=self.button_clicked),
                        ActionButton(text="-", button_clicked=self.button_clicked),
                    ]
                ),
                
                # Fourth row of digit buttons (1, 2, 3, +)
                ft.Row(
                    controls=[
                        DigitButton(text="1", button_clicked=self.button_clicked),
                        DigitButton(text="2", button_clicked=self.button_clicked),
                        DigitButton(text="3", button_clicked=self.button_clicked),
                        ActionButton(text="+", button_clicked=self.button_clicked),
                    ]
                ),
                
                # Fifth row (0 button spanning two columns, ., =)
                ft.Row(
                    controls=[
                        DigitButton(
                            text="0", expand=2, button_clicked=self.button_clicked
                        ),
                        DigitButton(text=".", button_clicked=self.button_clicked),
                        ActionButton(text="=", button_clicked=self.button_clicked),
                    ]
                ),
            ]
        )

    def button_clicked(self, e):
        """
        Handles button click events and updates the calculator display based on the button pressed.

        Args:
            e (Event): The click event object that contains information about the clicked button.
        """
        data = e.control.data  # Get the button's text (data)
        # print(f"Button clicked with data = {data}")

        # Reset or clear if 'AC' is pressed, or if there was an error in the previous operation
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()

        # Handle digit and decimal input
        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand is True:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data

        # Handle operator input (+, -, *, /)
        elif data in ("+", "-", "*", "/"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True

        # Handle equals button to perform the calculation
        elif data == "=":
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()

        # Handle percentage conversion
        elif data == "%":
            self.result.value = float(self.result.value) / 100
            self.reset()

        # Handle negation (+/-)
        elif data == "+/-":
            if float(self.result.value) > 0:
                self.result.value = "-" + str(self.result.value)
            elif float(self.result.value) < 0:
                self.result.value = str(self.format_number(abs(float(self.result.value))))

        self.update()  # Update the display with the new result

    def format_number(self, num):
        """
        Formats a number to remove the decimal if it's an integer, otherwise keeps the decimal.

        Args:
            num (float): The number to format.

        Returns:
            int or float: Returns an integer if the number is whole, otherwise returns the number as a float.
        """
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):
        """
        Performs arithmetic calculations based on the provided operator.

        Args:
            operand1 (float): The first operand for the calculation.
            operand2 (float): The second operand for the calculation.
            operator (str): The arithmetic operator to apply ('+', '-', '*', '/').

        Returns:
            int, float, or str: The result of the calculation or "Error" in case of division by zero.
        """
        if operator == "+":
            return self.format_number(operand1 + operand2)

        elif operator == "-":
            return self.format_number(operand1 - operand2)

        elif operator == "*":
            return self.format_number(operand1 * operand2)

        elif operator == "/":
            if operand2 == 0:
                return "Error"  # Handle division by zero
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        """
        Resets the calculator to its initial state, clearing the operator, operand, and flags.
        """
        self.operator = "+"  # Default operator
        self.operand1 = 0  # Reset the first operand
        self.new_operand = True  # Indicates that a new operand is ready for input
