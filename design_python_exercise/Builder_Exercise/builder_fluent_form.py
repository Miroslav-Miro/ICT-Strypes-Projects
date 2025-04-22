from typing import List


class FormBuilder:
    def __init__(self, login_form: str):
        """
        Initializes the FormBuilder with the name of the form class.
        Args:
            login_form (str): The name of the form class to be generated.
        """
        self.login_form: str = login_form
        self.fields: List[str] = []
        self.validators: List[str] = []

    def add_field(self, name: str, value: str) -> "FormBuilder":
        """
        Adds a field to the form's __init__ method.
        Args:
            name (str): The name of the field (e.g., 'username').
            value (str): The default value of the field (e.g., "''" for an empty string).
        Returns:
            FormBuilder: The current instance (to allow method chaining).
        """
        self.fields.append(f"    self.{name} = {value}")
        return self

    def add_validator(self, name: str, value: str) -> "FormBuilder":
        """
        Adds a validation condition for a field.
        Args:
            name (str): The name of the field (not currently used directly).
            value (str): The validation expression as a string (e.g., 'len(self.username) > 0').
        Returns:
            FormBuilder: The current instance (to allow method chaining).
        """
        self.validators.append(f"{value}")
        return self

    def __str__(self) -> str:
        """
        Constructs the source code of the form class as a string.
        Returns:
            str: The formatted Python class definition including fields and validation logic.
        """
        lines: List[str] = [f"class {self.login_form}:"]

        # Constructor with fields
        lines.append("  def __init__(self):")
        lines.extend(self.fields)

        # Validation method
        lines.append("")
        lines.append("  def validate(self):")
        joined = " and ".join(self.validators)
        lines.append(f"    return {joined}")

        return "\n".join(lines)


# Example usage
form = (
    FormBuilder("LoginForm")
    .add_field("username", "''")
    .add_field("password", "''")
    .add_validator("username", "len(self.username) > 0")
    .add_validator("password", "len(self.password) >= 6")
)

print(form)
