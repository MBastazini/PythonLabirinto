import pygame

class TitleScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = (126, 217, 81)  # Black background
        self.text_color = (28, 77, 5)
        self.title_font = pygame.font.Font("assets/fonts/fontBold.ttf", 74)
        self.subtitle_font = pygame.font.Font("assets/fonts/AmaticSC-Regular.ttf", 36)
        self.title_text = "Labirintomaxxing"
        self.subtitle_text = "Press Enter to Start"

        self.startGame = False

    def draw(self, screen):
        # Fill the background
        screen.fill(self.background_color)

        # Render title and subtitle
        title_surface = self.title_font.render(self.title_text, True, self.text_color)
        subtitle_surface = self.subtitle_font.render(self.subtitle_text, True, self.text_color)

        # Center the title and subtitle
        title_rect = title_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 20))
        subtitle_rect = subtitle_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 30))

        # Draw the title and subtitle on the screen
        screen.blit(title_surface, title_rect)
        screen.blit(subtitle_surface, subtitle_rect)
    
    def uptade(self):
        if(userInput()):
            self.startGame = True

def userInput():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        return True  # Start the game
    return False  # Continue showing the title screen
 