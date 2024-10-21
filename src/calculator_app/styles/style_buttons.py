import flet as ft


# Base class for creating calculator buttons
class CalcButton(ft.ElevatedButton):
    """
    A base class for creating a calculator button. Inherits from `ft.ElevatedButton` and
    sets common properties for the button.

    Attributes:
        text (str): The text to be displayed on the button.
        button_clicked (function): A callback function to be triggered when the button is clicked.
        expand (int): Optional; determines how much the button expands in the layout. Default is 1.
    """

    def __init__(self, text, button_clicked, expand=1):
        """
        Initializes the CalcButton class with text, a click event handler, and expansion properties.

        Args:
            text (str): The text label for the button.
            button_clicked (function): The function to be called when the button is clicked.
            expand (int): Optional; defines the expansion ratio of the button in the layout. Default is 1.
        """
        super().__init__()  # Call the parent class (ft.ElevatedButton) initializer
        self.text = text  # Set the button's text
        self.expand = expand  # Set the button's expansion in the layout
        self.on_click = (
            button_clicked  # Assign the callback function for the button click event
        )
        self.data = text  # Store the text as data, which can be used for other purposes


# Class for creating digit buttons
class DigitButton(CalcButton):
    """
    A subclass of CalcButton specifically for digit buttons (0-9).
    Digit buttons have specific background and text colors.
    """

    def __init__(self, text, button_clicked, expand=1):
        """
        Initializes a DigitButton with a white background and white text color.

        Args:
            text (str): The digit to be displayed on the button.
            button_clicked (function): The function to be called when the button is clicked.
            expand (int): Optional; defines the expansion ratio of the button in the layout. Default is 1.
        """
        CalcButton.__init__(
            self, text, button_clicked, expand
        )  # Initialize the base class
        self.bgcolor = ft.colors.WHITE24  # Set the button's background color
        self.color = ft.colors.WHITE  # Set the button's text color


# Class for creating action buttons (+, -, *, /, etc.)
class ActionButton(CalcButton):
    """
    A subclass of CalcButton specifically for action buttons (such as +, -, *, /).
    Action buttons have a specific orange background and white text color.
    """

    def __init__(self, text, button_clicked):
        """
        Initializes an ActionButton with an orange background and white text color.

        Args:
            text (str): The action symbol to be displayed on the button.
            button_clicked (function): The function to be called when the button is clicked.
        """
        CalcButton.__init__(self, text, button_clicked)  # Initialize the base class
        self.bgcolor = ft.colors.ORANGE  # Set the button's background color
        self.color = ft.colors.WHITE  # Set the button's text color


# Class for creating extra action buttons (such as Clear, =, etc.)
class ExtraActionButton(CalcButton):
    """
    A subclass of CalcButton specifically for extra action buttons (such as Clear, =, etc.).
    Extra action buttons have a specific light blue-gray background and black text color.
    """

    def __init__(self, text, button_clicked):
        """
        Initializes an ExtraActionButton with a light blue-gray background and black text color.

        Args:
            text (str): The action label (such as Clear or =) to be displayed on the button.
            button_clicked (function): The function to be called when the button is clicked.
        """
        CalcButton.__init__(self, text, button_clicked)  # Initialize the base class
        self.bgcolor = ft.colors.BLUE_GREY_100  # Set the button's background color
        self.color = ft.colors.BLACK  # Set the button's text color
