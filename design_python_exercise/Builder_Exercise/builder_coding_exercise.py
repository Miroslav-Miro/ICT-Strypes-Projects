from typing import List, Tuple


class CodeBuilder:
    def __init__(self, root_name: str) -> None:
        """
        Initializes a CodeBuilder for a given class name.
        Args:
            root_name (str): The name of the class to generate.
        """
        self.root_name: str = root_name
        self.fields: List[Tuple[str, str]] = []

    def add_field(self, name: str, value: str) -> "CodeBuilder":
        """
        Adds a field to the class.
        Args:
            name (str): Field name.
            value (str): Field value or default.
        Returns:
            CodeBuilder: The current instance for chaining.
        """
        self.fields.append((name, value))
        return self

    def __str__(self) -> str:
        """
        Generates the class definition as a string.
        Returns:
            str: The class code.
        """
        lines: List[str] = [f"class {self.root_name}:"]

        if not self.fields:
            lines.append("  def __init__(self):")
            lines.append("    pass")
        else:
            lines.append("  def __init__(self):")
            for name, value in self.fields:
                lines.append(f"    self.{name} = {value}")

        return "\n".join(lines)


# Example usage
cb = CodeBuilder("Person").add_field("name", '""').add_field("age", "0")
print(cb)
