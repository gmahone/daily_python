import random
class Ghost(object):
    def __init__(self):
        color_list = ["white", "yellow", "purple", "red"]
        self.color = color_list[random.randint(0,3)]
