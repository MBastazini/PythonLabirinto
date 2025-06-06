from util import Button, TextBox
import pygame

class TitleScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = (126, 217, 81)
        self.nextScreen = None

        padding_top = 30
        padding = 30
        #botão de jogar
        self.titleText = TextBox(
            position=(self.screen_width // 2 - 200, self.screen_height // 2 - 100),
            size=(400, 100),
            text="Maze Game",
            font=2,
            text_color=(28, 77, 5),
            background_color=False  # no background
        )
        self.bPlay = Button(
            text="Play",
            size=(200, 50),
            position=(self.screen_width // 2 - 100, self.screen_height // 2 + padding_top),
            onClick=self.start_game
        )
        self.bScores = Button(
            text="Scores",
            size=(200, 50),
            position=(self.screen_width // 2 - 100, self.screen_height // 2 + padding_top + padding + self.bPlay.size[1]),
            onClick=self.show_scores
        )

    def draw(self, screen):
        screen.fill(self.background_color)

        # Draw title text
        self.titleText.draw(screen)

        # Draw buttons 
        self.bPlay.draw(screen)
        self.bScores.draw(screen)

    def update(self, screen, events):
        self.bPlay.update(events)
        self.bScores.update(events)
        self.draw(screen)

    def start_game(self):
        self.nextScreen = 'level_selector'
    
    def show_scores(self):
        self.nextScreen = 'scores'