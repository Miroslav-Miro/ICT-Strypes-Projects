class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
  
    def  __init__(self):
        self.counter = 0
        
    def create_person(self, name):
        p = Person(self.counter, name)
        self.counter += 1

        return p
    