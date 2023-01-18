class Block:
    def __init__(self, dims):
        self.width = dims[0]
        self.length = dims[1]
        self.height = dims[2]
        
    def get_width(self):
        return self.width
    
    def get_length(self):
        return self.length
    
    def get_height(self):
        return self.height
    
    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self):
        front_back = 2 * self.length * self.height
        left_right = 2 * self.width * self.height
        top_bottom = 2 * self.width * self.length
        return front_back + left_right + top_bottom

    
# best practice
class Block:
    def __init__(self, values):
        self._width = values[0]
        self._length = values[1]
        self._height = values[2]
    
    def get_width(self):
        return self._width

    def get_length(self):
        return self._length
    
    def get_height(self):
        return self._height
    
    def get_volume(self):
        return self.get_width()*self.get_length()*self.get_height()
    
    def get_surface_area(self):
        return 2*(self.get_width()*self.get_height()
                  + self.get_width()*self.get_length()
                  + self.get_length()*self.get_height())
