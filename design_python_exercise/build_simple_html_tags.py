class HtmlBuilder:
    def __init__(self, root_param):
        """
        Initializes the HtmlBuilder with a root HTML tag.
        Args:
            root_param (str): The root HTML element (e.g., 'ul', 'div').
        """
        self.root_param = root_param
        self.fields = []
    
    def add_child(self, param, item):
        """
        Adds a child HTML element with the given tag and content.
        Args:
            param (str): The child HTML tag (e.g., 'li', 'span').
            item (str): The content to place inside the child tag.
        Returns:
            self: Allows method chaining.
        """
        self.fields.append((param, item))
        return self
    
    def __str__(self):
        """
        Builds and returns the HTML structure as a formatted string.
        Returns:
            str: The generated HTML.
        """
        lines = [f'<{self.root_param}>']
        
        for param, item in self.fields:
            lines.append(f'  <{param}>{item}</{param}>')
        
        lines.append(f'</{self.root_param}>')
        
        return '\n'.join(lines)


# Example usage
builder = HtmlBuilder("ul")
builder.add_child("li", "Item 1").add_child("li", "Item 2")
print(builder)
