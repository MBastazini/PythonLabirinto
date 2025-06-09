from util import Button, TextBox
import pygame

class TitleScreen:
    def __init__(self, screen_width, screen_height, player_file):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = (126, 217, 81)
        self.nextScreen = None

        self.active_player_name = player_file.readlines()[0].replace("\n", "") if player_file else "Player"

        padding_top = 30
        padding = 30
        #botão de jogar

        self.active_player_text = TextBox(
            position=(self.screen_width // 2 - 200, 50),
            size=(400, 50),
            text=f"Active Player: {self.active_player_name}",
            font=1,
            text_color=(28, 77, 5),
            background_color=False  # no background
        )

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
        self.bNewPlayer = Button(
            text="Save files",
            size=(200, 50),
            position=(self.screen_width // 2 - 100, self.screen_height // 2 + padding_top + padding * 2 + self.bPlay.size[1] + self.bScores.size[1]),
            onClick=lambda: setattr(self, 'nextScreen', 'save_files')
        )

    def draw(self, screen):
        screen.fill(self.background_color)

        # Draw title text
        self.titleText.draw(screen)
        # Draw active player text
        self.active_player_text.draw(screen)

        # Draw buttons 
        self.bPlay.draw(screen)
        self.bScores.draw(screen)
        self.bNewPlayer.draw(screen)

    def update(self, screen, events):
        self.bPlay.update(events)
        self.bScores.update(events)
        self.bNewPlayer.update(events)
        self.draw(screen)

    def start_game(self):
        self.nextScreen = 'level_selector'
    
    def show_scores(self):
        self.nextScreen = 'scores'