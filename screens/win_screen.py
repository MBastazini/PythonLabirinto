import pygame
from util import TextBox, Button

class WinScreen:
    def __init__(self, screen_width, screen_height, elapsed_time=0, player_score=0):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = (126, 217, 81)
        self.text_color = (28, 77, 5)
        self.next_screen = None
        self.player_score = player_score
        self.elapsed_time_text_box = TextBox(
            position=(self.screen_width // 2 - 200, self.screen_height // 2 - 100),
            size=(400, 50),
            text=f"Time: {elapsed_time:.1f} seconds",
            font=1,
            text_color=self.text_color,
            background_color=False  # no background
        )
        self.player_score_text_box = TextBox(
            position=(self.screen_width // 2 - 200, self.screen_height // 2 - 50),
            size=(400, 50),
            text=f"Score: {player_score}",
            font=1,
            text_color=self.text_color,
            background_color=False  # no background
        )
        self.title = TextBox(
            position=(self.screen_width // 2 - 200, 50),
            size=(400, 100),
            text="You Win!",
            font=2,
            text_color=self.text_color,
            background_color=False  # no background
        )

        self.play_again_button = Button(
            text="Play Again",
            size=(200, 50),
            position=(self.screen_width // 2 - 100, self.screen_height // 2 + 25),
            onClick=self.play_again
        )

    def draw(self, screen):
        screen.fill(self.background_color)

        # Draw title
        self.title.draw(screen)
        # Draw elapsed time
        self.elapsed_time_text_box.draw(screen)

        # Draw play again button
        self.play_again_button.draw(screen)
        # Draw player score
        self.player_score_text_box.draw(screen)

    def update(self, screen, events):
        
        self.play_again_button.update(events)
        self.draw(screen)


    def play_again(self):
        self.next_screen = 'level_selector'