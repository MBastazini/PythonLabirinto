import pygame
import settings
from util import Button, TextBox, InputBox

class NewPlayerScreen:
    def __init__(self, screen_width, screen_height, file_name='saves/players/player_1.txt', active_save_file=1):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = (126, 217, 81)
        self.text_color = (28, 77, 5)
        self.next_screen = None
        self.active_save_file = active_save_file

        self.file_name = file_name
        
        self.title = TextBox(
            position=(self.screen_width // 2 - 200, 50),
            size=(400, 100),
            text="New Player",
            font=2,
            text_color=self.text_color,
            background_color=False  # no background
        )

        self.name_input_box = InputBox(
            position=(self.screen_width // 2 - 200, self.screen_height // 2 - 50),
            size=(400, 50),
            font=1,
            text_color=self.text_color,
            background_color=(255, 255, 255)  # white background
        )

        self.start_button = Button(
            text="Start Game",
            size=(200, 50),
            position=(self.screen_width // 2 - 100, self.screen_height // 2 + 20),
            onClick=self.start_game
        )

    def draw(self, screen):
        screen.fill(self.background_color)

        # Draw title
        self.title.draw(screen)
        # Draw name input box
        self.name_input_box.draw(screen)
        # Draw start button
        self.start_button.draw(screen)

    def update(self, screen, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.start_game()

        self.start_button.update(events)
        self.name_input_box.update(events)
        self.draw(screen)

        #print(f"Current player name: {self.name_input_box.text.strip()}")

    def start_game(self):
        player_name = self.name_input_box.text.strip()
        if player_name:
            f = open(self.file_name, 'w')
            f.write("1 \n")
            f.write(f"{player_name} \n")
            f.close()

            settings.active_save_file = self.active_save_file
            settings.save_files[self.active_save_file-1][0] = 1
            settings.save_files[self.active_save_file-1][1] = player_name

            print(f"Starting game for player: {player_name}")
            self.next_screen = 'title'
    
    def change_file_path(self, new_file_path):
        self.active_save_file = settings.active_save_file
        self.file_name = new_file_path
        self.name_input_box.text = ""