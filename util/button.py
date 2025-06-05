class Button:
    def __init__(self, size, position, color, color_hover):
        self.size = (size[0], size[1])
        self.position = position
        self.color_default = color
        self.color_hover = color_hover