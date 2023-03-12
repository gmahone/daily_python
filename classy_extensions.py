from preloaded import Animal

class Cat(Animal):
    def speak(this):
        name = this.name
        return f"{name} meows."

    
# using proper self rather than this
class Cat(Animal):
    def speak(self):
        return self.name + ' meows.'
