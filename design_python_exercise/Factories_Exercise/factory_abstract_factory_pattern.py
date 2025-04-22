from abc import ABC, abstractmethod
from typing import Optional


class UIComponentFactory(ABC):
    """
    Abstract Factory interface that declares methods for creating UI components.
    """

    @abstractmethod
    def create_button(self) -> str:
        """
        Create a themed button.
        Returns:
            str: A string representing a button.
        """
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def create_text_field(self) -> str:
        """
        Create a themed text field.
        Returns:
            str: A string representing a text field.
        """
        raise NotImplementedError("Subclasses must implement this method")


class DarkTheme(UIComponentFactory):
    """
    Concrete factory for creating dark-themed UI components.
    """

    def create_button(self) -> str:
        """
        Create a dark-themed button.
        Returns:
            str: 'Dark Button'
        """
        return "Dark Button"

    def create_text_field(self) -> str:
        """
        Create a dark-themed text field.
        Returns:
            str: 'Dark text fields'
        """
        return "Dark text fields"


class LightTheme(UIComponentFactory):
    """
    Concrete factory for creating light-themed UI components.
    """

    def create_button(self) -> str:
        """
        Create a light-themed button.
        Returns:
            str: 'Light Button'
        """
        return "Light Button"

    def create_text_field(self) -> str:
        """
        Create a light-themed text field.
        Returns:
            str: 'Light text fields'
        """
        return "Light text fields"


class DarkThemeFactory:
    """
    Factory class to retrieve specific dark-themed UI components.
    """

    @staticmethod
    def get_type(data: str) -> Optional[str]:
        """
        Returns a dark-themed UI component based on the type specified.
        Args:
            data (str): The type of UI component ('Button' or 'Text Field').
        Returns:
            Optional[str]: The corresponding UI component string or None if type is unknown.
        """
        dark_theme = DarkTheme()
        if data == "Button":
            return dark_theme.create_button()
        elif data == "Text Field":
            return dark_theme.create_text_field()
        return None


class LightThemeFactory:
    """
    Factory class to retrieve specific light-themed UI components.
    """

    @staticmethod
    def get_type(data: str) -> Optional[str]:
        """
        Returns a light-themed UI component based on the type specified.
        Args:
            data (str): The type of UI component ('Button' or 'Text Field').
        Returns:
            Optional[str]: The corresponding UI component string or None if type is unknown.
        """
        light_theme = LightTheme()
        if data == "Button":
            return light_theme.create_button()
        elif data == "Text Field":
            return light_theme.create_text_field()
        return None


# Example usage
dark_button = DarkThemeFactory.get_type("Button")
light_text = LightThemeFactory.get_type("Text Field")

print(dark_button)  # Dark Button
print(light_text)  # Light text fields
