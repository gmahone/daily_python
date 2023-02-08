class Dog ():
  def __init__(self, breed):
    self.breed = breed
    
  def bark(self):
    return "Woof"
    

snoopy = Dog("Beagle")

scoobydoo = Dog("Great Dane")


# using staticmethod
class Dog ():
    def __init__(self, breed):
        self.breed = breed
    
    @staticmethod
    def bark():
        return "Woof"
    
snoopy = Dog("Beagle")

scoobydoo = Dog("Great Dane")
