import pygame
from .button import Button
from .text_box import TextBox

class AreYouSureSurface:
    def __init__(self, screen_width, screen_height, confirmAction: callable, cancelAction: callable, customMessage = None):
        self.active = False
        self.confirmAction = confirmAction
        self.cancelAction = cancelAction
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.newSurface = pygame.Surface((self.screen_width, self.screen_height))
        self.newSurface.fill((255,255,255))
        self.background_color = (126, 217, 81)
        self.text_color = (28, 77, 5)
        self.customMessage = customMessage

        self.are_you_sure_text = TextBox(
            text="Are you sure?",
            position=(self.screen_width // 2 - 150, self.screen_height // 2 - 120),
            size=(300, 50),
            text_color=self.text_color,
            font=1
        )

        self.customMessage_text = TextBox(
            text=self.customMessage if self.customMessage else "",
            position=(self.screen_width // 2 - 150, self.screen_height // 2 - 50),
            size=(300, 50),
            text_color=self.text_color,
            font=1
        )

        self.yes_button = Button(
            text="Yes",
            onClick=self.confirm_action,
            size=(100, 50),
            position=(self.screen_width // 2 - 150, self.screen_height // 2 + 20)
        )

        self.no_button = Button(
            text="No",
            onClick=self.cancel_action,
            size=(100, 50),
            position=(self.screen_width // 2 + 50, self.screen_height // 2 + 20)
        )

    def confirm_action(self):
        self.confirmAction()
        # Implement the action to be confirmed here

    def cancel_action(self):
        self.cancelAction()
        # Implement the cancellation logic here

    def draw(self):
        self.are_you_sure_text.draw(self.newSurface)
        self.customMessage_text.draw(self.newSurface)
        self.yes_button.draw(self.newSurface)
        self.no_button.draw(self.newSurface)

    def update(self, screen, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.cancel_action()

        if self.active:
            self.draw()
            self.yes_button.update(events)
            self.no_button.update(events)
            screen.blit(self.newSurface, (0, 0))

    def toggle(self):
        self.active = not self.active