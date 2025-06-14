from util import Button, TextBox, BackButton
import pygame

class NewLevelScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = (126, 217, 81)
        self.text_color = (28, 77, 5)
        self.startGame = False
        self.difficulty = 1  # Default difficulty

        self.next_screen = None
        self.back_button = BackButton(
            onClick=lambda: setattr(self, 'next_screen', 'level_selector')
        )

        self.title = TextBox(
            position=(self.screen_width // 2 - 200, 50),
            size=(400, 100),
            text="Select Level",
            font=2,
            text_color=self.text_color,
            background_color=False  # no background
        )

        self.level_buttons = [
            Button(
                text=str(i),
                size=(200, 50),
                position=(self.screen_width // 2 - 100, self.screen_height // 2 - 100 + i * 60),
                onClick=lambda i=i: self.level_selected(i)
            )
            for i in range(1, 4)
        ]

    def draw(self, screen):
        screen.fill(self.background_color)

        # Draw title
        self.title.draw(screen)
        # Draw back button
        self.back_button.draw(screen)

        # Draw level buttons
        for button in self.level_buttons:
            button.draw(screen)

    def update(self, screen, events):
        for button in self.level_buttons:
            button.update(events)
        self.back_button.update(events)
        self.draw(screen)

    def level_selected(self, level):
        self.difficulty = level
        self.startGame = True