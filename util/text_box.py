import pygame

class TextBox:
    def __init__(self, position, size, font = 1, text="", text_color=(0, 0, 0), background_color=(255, 255, 255)):
        self.position = position
        self.size = size
        match font:
            case 1:
                self.font = pygame.font.Font("assets/fonts/AmaticSC-Regular.ttf", 36)
            case 2:
                self.font = pygame.font.Font("assets/fonts/fontBold.ttf", 74)
            case _:
                self.font = pygame.font.Font("assets/fonts/AmaticSC-Regular.ttf", 36)
        self.text = text

        self.text_color = text_color
        self.background_color = background_color
        self.padding = 10 #for the background rectangle

    def draw(self, screen):
        # Draw the background
        if self.background_color:
            # Draw a rectangle for the background, if there is a background
            background_rect = pygame.Rect(self.position[0]-self.padding, self.position[1]-self.padding, self.size[0]+self.padding*2, self.size[1]+self.padding*2)
            pygame.draw.rect(screen, self.background_color, background_rect)
        # Render the text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.position[0] + self.size[0] // 2, self.position[1] + self.size[1] // 2))
        screen.blit(text_surface, text_rect)
        
    def set_text(self, text):
        self.text = text