from typing import List, Tuple

class HtmlBuilder:
    def __init__(self, root_param: str) -> None:
        """
        Initializes the HtmlBuilder with a root HTML tag.
        Args:
            root_param (str): The root HTML element tag (e.g., 'ul', 'div').
        """
        self.root_param: str = root_param
        self.fields: List[Tuple[str, str]] = []
    
    def add_child(self, param: str, item: str) -> 'HtmlBuilder':
        """
        Adds a child HTML element inside the root tag.
        Args:
            param (str): The tag name of the child (e.g., 'li').
            item (str): The content inside the child tag.
        Returns:
            HtmlBuilder: The current instance for chaining.
        """
        self.fields.append((param, item))
        return self
    
    def __str__(self) -> str:
        """
        Builds and returns the HTML structure as a string.
        Returns:
            str: The generated HTML code.
        """
        lines: List[str] = [f'<{self.root_param}>']
        
        for param, item in self.fields:
            lines.append(f'  <{param}>{item}</{param}>')
        
        lines.append(f'</{self.root_param}>')
        return '\n'.join(lines)


# Example usage
builder = HtmlBuilder("ul")
builder.add_child("li", "Item 1").add_child("li", "Item 2")
print(builder)
