class CodeBuilder:
    def __init__(self, root_name):
        """
        Initializes the CodeBuilder with a class name and an empty list of fields.
        Args:
            root_name (str): The name of the class to be generated.
        """
        self.root_name = root_name
        self.fields = []
        
    def add_field(self, name, type):
        """
        Adds a field to the class with the given name and type/value.
        Args:
            name (str): The name of the field.
            type (str): The type or default value of the field (e.g., '0', '""', '[]').
        Returns:
            self: Allows method chaining.
        """
        self.fields.append((name, type))
        return self
    
    def __str__(self):
        """
        Builds and returns the Python class definition as a string.
        Returns:
            str: The formatted class definition.
        """
        lines = [f"class {self.root_name}:"]
        
        if not self.fields:
            lines.append("  def __init__(self):")
            lines.append("    pass")
        else:
            lines.append("  def __init__(self):")
            for name, value in self.fields:
                lines.append(f"    self.{name} = {value}")
        
        return '\n'.join(lines)


# Example usage
cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
print(cb)
