class Shape:
  def __init__(self):
    pass
  
class Square(Shape):
  def __init__(self):
    super().__init__()
    
  def __str__(self):
    return 'Square'
    
class Circle(Shape):
  def __init__(self):
    super().__init__()
    
  def __str__(self):
    return "Circle"
    
class ShapeFactory():
  
  def create_shape(self, shape_type):
    if shape_type == 'Circle':
      return Circle()
    elif shape_type == 'Square':
      return Square()