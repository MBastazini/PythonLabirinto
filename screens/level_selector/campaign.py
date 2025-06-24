from util import Button, TextBox, BackButton
import pygame

class CampaignScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = (126, 217, 81)
        self.text_color = (28, 77, 5)
        self.next_screen = None

        self.title = TextBox(
            position=(self.screen_width // 2 - 200, 50),
            size=(400, 100),
            text="Campaign",
            font=2,
            text_color=self.text_color,
            background_color=False  # no background
        )
        self.back_button = BackButton(
            onClick=self.back_to_level_selector
        )
        self.level_buttons = []

        #tenta abrir o arquivo de cache (diz quantas fases existem)
        try:
            with open("saves/fases/cache.txt", "r") as cache_file:
                lines = cache_file.readlines()
                #print(f"Cache file found: {lines}")
                self.level_count = int(lines[0].strip())
        except (FileNotFoundError, ValueError):
            self.level_count = 0

        #determina o padding inicial pra deixar os botões centralizados
        total_button_size = 50 * 4 + 50 * 3  # 4 buttons, each 50px tall, with 100px spacing
        initial_padding = (self.screen_width - total_button_size) // 2
        count = 1
        for i in range(0, 4):
            for j in range(0, 4):
                if count > self.level_count:
                    break
                newBtn = Button(
                    text=f"{count}",
                    size=(50, 50),
                    position=(initial_padding + (100*j), (self.screen_width // 2 - 100) + (100*i)),
                    onClick=lambda level=count: self.select_level(level),
                    color= (255, 255, 255) if True else (51, 204, 51)  # Default color
                )
                count += 1
                self.level_buttons.append(newBtn)

    def select_level(self, level):
        #print(f"Selected level: {level}")
        self.next_screen = f"fase{level}" #nome do arquivo da fase

    def back_to_level_selector(self):
        self.next_screen = "level_selector"

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