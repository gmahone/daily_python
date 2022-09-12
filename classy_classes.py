class Person:
    def __init__(self, name, age):
        self.info="{name}s age is {age}".format(name = name, age = age)

# add solution with f instead of format
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"
   
## better separation
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def info(self):
        return '{}s age is {}'.format(self.name, self.age)
