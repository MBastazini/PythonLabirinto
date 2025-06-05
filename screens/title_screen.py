from util import Button, TextBox
import pygame

class TitleScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = (126, 217, 81)
        self.startGame = False

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
        self.bPlay = Button((200, 50), (self.screen_width // 2 - 100, self.screen_height // 2 + padding_top), 
                            (255, 255, 255), (200, 255, 200), "Play", self.start_game)
        self.bScores = Button((200, 50), (self.screen_width // 2 - 100, self.screen_height // 2 + padding_top + padding + self.bPlay.size[1]), 
                              (255, 255, 255), (200, 255, 200), "Scores", self.show_scores)

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
        self.startGame = True
    
    def show_scores(self):
        print("Show scores clicked")