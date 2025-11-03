class Parent:
    def __init__(self):
        self.data = 'this is a public attribute'
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = 'this is a private attribute'


c = Child()
print(c.data)
print(c.__data)  # This will raise an AttributeError