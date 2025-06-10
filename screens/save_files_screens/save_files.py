from util import Button, TextBox, BackButton
import settings
import pygame

#creates a screen with 3 buttons (3 save files) and a back button
class SaveFilesScreen:
    def __init__(self, screen_width, screen_height):
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = (126, 217, 81)
        self.text_color = (28, 77, 5)
        self.next_screen = None

        self.title = TextBox(
            position=(self.screen_width // 2 - 200, 50),
            size=(400, 100),
            text="Save Files",
            font=2,
            text_color=self.text_color,
            background_color=False  # no background
        )

        self.save_buttons = [
            Button(
                text=(settings.save_files[i][1] if settings.save_files[i][0] else f"New save file"),
                size=(200, 50),
                position=(self.screen_width // 2 - 100, self.screen_height // 2 - 100 + i * 60),
                onClick=lambda i=i: self.select_save_file(i),
                color=(255, 0, 0) if i + 1 == settings.active_save_file else (200, 255, 200),
                color_hover=(255, 100, 100) if i + 1 == settings.active_save_file else (150, 200, 150)

            ) for i in range(3)
        ]

        self.back_button = BackButton(
            onClick=lambda: setattr(self, 'next_screen', 'title')
        )

        #test to see witch save files exist and witch don't
    def select_save_file(self, file_index):
        settings.active_save_file = file_index+1
        print(f"Selected Save File {settings.active_save_file}")
        self.next_screen = 'title'
        # Here you can add logic to load the selected save file

    def draw(self, screen):
        screen.fill(self.background_color)

        # Draw title
        self.title.draw(screen)

        # Draw save buttons
        for button in self.save_buttons:
            button.draw(screen)

        # Draw back button
        self.back_button.draw(screen)
    
    def update(self, screen, events):
        for button in self.save_buttons:
            button.update(events)
        self.back_button.update(events)
        self.draw(screen)

        # Check if next screen is set
        if self.next_screen:
            return self.next_screen
        return None