from .text_box import TextBox
import pygame

class BackButton:
    def __init__(self, onClick: callable, color=(255, 255, 255), color_hover=(200, 200, 200)):
        self.size = (100, 50)
        self.position = (10, 10)
        self.color_default = color
        self.color_hover = color_hover
        #texto fica no meio do botão
        self.text = TextBox(
            position=(0, 0),
            size=(self.size[0], self.size[1]),
            text="Back",
            font=1,
            text_color=(0, 0, 0),
            background_color=False #no background
        )
        self.onClick = onClick

    def is_hovering(self):
        mouse_pos = pygame.mouse.get_pos()
        x, y = self.position
        width, height = self.size
        return (x <= mouse_pos[0] <= x + width) and (y <= mouse_pos[1] <= y + height)

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.is_hovering():
                    self.onClick()


    def draw(self, screen):
        color = self.color_hover if self.is_hovering() else self.color_default
        button_surface = pygame.Surface(self.size)
        button_surface.fill(color)
        self.text.draw(button_surface)
        screen.blit(button_surface, self.position)