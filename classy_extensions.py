from preloaded import Animal

class Cat(Animal):
    def speak(this):
        name = this.name
        return f"{name} meows."

    
# using proper self rather than this
class Cat(Animal):
    def speak(self):
        return self.name + ' meows.'

# using string formatting
class Cat(Animal):   
    def speak(self):
        return '{} meows.'.format(self.name)

    
# using an init method
class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return '{} meows.'.format(self.name)
