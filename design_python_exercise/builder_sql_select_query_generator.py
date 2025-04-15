from typing import List

class QueryBuilder:
    def __init__(self) -> None:
        """
        Initializes a new instance of QueryBuilder with empty columns,
        table name, and condition.
        """
        self.columns: List[str] = []
        self.table_name: str = ''
        self.condition: str = ''
  
    def select(self, *fields: str) -> 'QueryBuilder':
        """
        Specifies the columns to be selected in the SQL query.
        Args:
            fields (str): Variable number of column names.
        Returns:
            QueryBuilder: The current instance for chaining.
        """
        self.columns.extend(fields)
        return self
  
    def from_table(self, table_name: str) -> 'QueryBuilder':
        """
        Sets the table name for the SQL query.
        Args:
            table_name (str): The name of the table.
        Returns:
            QueryBuilder: The current instance for chaining.
        """
        self.table_name = table_name
        return self
  
    def where(self, condition: str) -> 'QueryBuilder':
        """
        Sets the WHERE condition for the SQL query.
        Args:
            condition (str): A SQL condition string.
        Returns:
            QueryBuilder: The current instance for chaining.
        """
        self.condition = condition
        return self
  
    def __str__(self) -> str:
        """
        Returns the constructed SQL query as a string.
        Returns:
            str: The formatted SQL query.
        """
        lines: List[str] = ['SELECT']
        
        for i, column in enumerate(self.columns):
            suffix = ',' if i < len(self.columns) - 1 else ''
            lines.append(f'{column}{suffix}')
        
        lines.append('FROM')
        lines.append(self.table_name)
        
        if self.condition:
            lines.append(f'WHERE {self.condition}')
        
        return ' '.join(lines)


# Example usage
query = QueryBuilder().select("name", "age").from_table("users").where("age > 18")
print(query)
