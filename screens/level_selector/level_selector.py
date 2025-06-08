from util import Button, TextBox, BackButton
import pygame

class LevelSelectorScreen:
   #divide the screen in two, at the right: when clicked change to "campaign screen", at the left, change to "NewLevel screen"
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = (126, 217, 81)
        self.text_color = (28, 77, 5)
        self.next_screen = None

        self.title = TextBox(
            position=(self.screen_width // 2 - 200, 50),
            size=(400, 100),
            text="Level Selector",
            font=2,
            text_color=self.text_color,
            background_color=False  # no background
        )

        self.campaign_button = Button(
            text="Campaign",
            size=(200, 50),
            position=(self.screen_width // 2 - 100, self.screen_height // 2 - 100),
            onClick=self.select_campaign
        )

        self.new_level_button = Button(
            text="New Level",
            size=(200, 50),
            position=(self.screen_width // 2 - 100, self.screen_height // 2 + 20),
            onClick=self.select_new_level
        )

        self.back_button = BackButton(
            onClick=
            lambda: setattr(self, 'next_screen', 'title')
        )

    def select_campaign(self):
        self.next_screen = "campaign"

    def select_new_level(self):
        self.next_screen = "new_level"

    def draw(self, screen):
        screen.fill(self.background_color)

        # Draw title
        self.title.draw(screen)

        # Draw buttons
        self.campaign_button.draw(screen)
        self.new_level_button.draw(screen)
        self.back_button.draw(screen)
    
    def update(self, screen, events):
        self.campaign_button.update(events)
        self.new_level_button.update(events)
        self.back_button.update(events)
        self.draw(screen)