import pygame
from util import Button, TextBox

class InputBox:
    def __init__(self, position, size, font, text_color, background_color):
        self.rect = pygame.Rect(position, size)
        match font:
            case 1:
                self.font = pygame.font.Font("assets/fonts/AmaticSC-Regular.ttf", 36)
            case 2:
                self.font = pygame.font.Font("assets/fonts/fontBold.ttf", 74)
            case _:
                self.font = pygame.font.Font("assets/fonts/AmaticSC-Regular.ttf", 36)
        self.text_color = text_color
        self.background_color = background_color
        self.text = ""
        self.active = False

    def draw(self, screen):
        if self.background_color:
            pygame.draw.rect(screen, self.background_color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode