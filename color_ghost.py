class Ghost(object):
    def __init__(self):
        color_list = ["white", "yellow", "purple", "red"]
        self.color = color_list[randint(0,3)]
