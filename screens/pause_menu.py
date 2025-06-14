import pygame
from util import Button, TextBox, AreYouSureSurface

class PauseMenu:
    def __init__(self, screen_width, screen_height):
        self.screen = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)  # Create a surface with alpha for transparency
        self.screen_width, self.screen_height = self.screen.get_size()

        #semi-transparent background
        #self.background_color = (126, 217, 81)
        self.background_color = (126, 217, 81, 128)  # RGBA for semi-transparency
        self.text_color = (28, 77, 5)
        self.screen.fill(self.background_color)
        self.text_box_size = (200, 50)
        self.text_box_position = (self.screen_width // 2 - self.text_box_size[0] // 2, 
                                  50)
        self.text_box = TextBox(
            text="Paused", 
            position=self.text_box_position, 
            size=self.text_box_size, 
            text_color=self.text_color, 
            background_color=(126, 217, 81), 
            font=2)
        # '*' symbol expands the tuple into positional arguments
        self.resume_button = None
        self.return_button = None
        self.quit_button = None
        self.create_buttons()

        self.isPaused = False
        self.events = []


        self.areYouSureSurface = AreYouSureSurface(screen_width, screen_height, self.quit_game, self.cancel_areYouSure)

    def create_buttons(self):
        self.resume_button = Button(
            text="Resume", 
            onClick=self.resume_game,
            size=(200, 50),
            position=(self.screen_width // 2 - 100, self.screen_height // 2 + 60)
        )
        self.return_button = Button(
            text="Return to Menu", 
            onClick=self.return_to_menu,
            size=(200, 50),
            position=(self.screen_width // 2 - 100, self.screen_height // 2 + 120)
        )
        self.quit_button = Button(
            text="Quit", 
            onClick=self.quit_game_1,
            size=(200, 50),
            position=(self.screen_width // 2 - 100, self.screen_height // 2 + 180)
        )

    def cancel_areYouSure(self):
        self.areYouSureSurface.toggle()

    def resume_game(self):
        self.isPaused = False

    def quit_game_1(self):
        self.areYouSureSurface.toggle()

    def quit_game(self):
        pygame.quit()
        exit()

    def return_to_menu(self):
        self.events.append('return_to_menu')

    def draw(self, screen):
        self.text_box.draw(self.screen)
        self.resume_button.draw(self.screen)
        self.return_button.draw(self.screen)
        self.quit_button.draw(self.screen)
        screen.blit(self.screen, (0, 0))
        


    def update(self, screen, events):
        if self.isPaused:
            self.resume_button.update(events)
            self.return_button.update(events)
            self.quit_button.update(events)
            self.draw(screen)

            if self.areYouSureSurface.active:
                self.areYouSureSurface.update(screen, events)
        
        return self.events
