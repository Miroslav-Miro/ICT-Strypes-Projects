class Conection:
  def __init__(self, name):
    self.name = name
    
class ConnectionFactory():
  def __init__(self):
    self.connections = {}
    
  def get_connection(self, name):
    if name in self.connections:
      return self.connections[name]
    else:
      connection = Conection(name)
      self.connections[name] = connection
      return self.connections[name]

factory = ConnectionFactory()

c1 = factory.get_connection("main_db")
c2 = factory.get_connection("cache")
c3 = factory.get_connection("main_db")

print(c1 is c3) 
print(c1.name)
print(c2.name)
