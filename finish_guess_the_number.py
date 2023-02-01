class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
  
    def guess(self,n):
        if n == self.number:
            return True
        else:
            self.lives -= 1
            return False
            
