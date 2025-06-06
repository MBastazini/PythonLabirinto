import pygame
from util import TextBox, Button
class ScoresScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.text_color = (0, 0, 0)
        self.text_box_position = (screen_width // 2 - 100, screen_height // 2 - 50)
        self.text_box_size = (200, 100)
        
        # Create a text box for the title
        self.text_box = TextBox(
            position=self.text_box_position,
            size=self.text_box_size,
            text="Scores",
            text_color=self.text_color,
            background_color=(255, 255, 255),
            font=2
        )

        self.scores = [100, 200, 300]  # Example scores, replace with actual score retrieval logic

    def draw(self, screen):
        screen.fill((255, 255, 255))
        self.text_box.draw(screen)
        # Here you would draw the scores, for now we just draw the title
        for i, score in enumerate(self.scores):
            score_text = TextBox(
                position=(self.text_box_position[0], self.text_box_position[1] + (i + 1) * 30),
                size=(self.text_box_size[0], 30),
                text=f"Score {i + 1}: {score}",
                text_color=self.text_color,
                background_color=(255, 255, 255),
                font=2
            )
            score_text.draw(screen)

    def update(self, screen, _):
        self.draw(screen)