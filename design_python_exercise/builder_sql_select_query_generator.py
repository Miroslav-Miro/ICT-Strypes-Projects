class QueryBuilder():
    def __init__(self):
        """
        Initializes a new instance of QueryBuilder with default empty values for columns,
        table name, and condition.
        """
        self.columns = []
        self.table_name = ''
        self.condition = ''
  
    def select(self, *fields):
        """
        Specifies the columns to be selected in the SQL query.
        Args:
            fields: A variable number of column names to select.
        Returns:
            self: Allows method chaining.
        """
        for field in fields:
            self.columns.append(field)
        return self
  
    def from_table(self, table_name):
        """
        Specifies the table name to select data from.
        Args:
            table_name (str): The name of the table.
        Returns:
            self: Allows method chaining.
        """
        self.table_name = table_name
        return self
  
    def where(self, condition):
        """
        Specifies the condition for the WHERE clause in the SQL query.
        Args:
            condition (str): A condition string (e.g., "age > 18").
        Returns:
            self: Allows method chaining.
        """
        self.condition = condition
        return self
  
    def __str__(self):
        """
        Constructs and returns the SQL query as a string.
        Returns:
            str: The formatted SQL query.
        """
        lines = ['SELECT']
        
        for column in self.columns:
            if column == self.columns[-1]:
                lines.append(column)
            else:
                lines.append(column + ',')
        
        lines.append('FROM')
        lines.append(f'{self.table_name}')
        lines.append(f'{self.condition}:')
        
        return ' '.join(lines)

# Example usage
query = QueryBuilder().select("name", "age").from_table("users").where("age > 18")
print(query)
