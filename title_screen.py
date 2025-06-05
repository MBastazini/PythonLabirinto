from util import Button
import pygame

class TitleScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = (126, 217, 81)
        self.text_color = (28, 77, 5)
        self.title_font = pygame.font.Font("assets/fonts/fontBold.ttf", 74)
        self.regular_font = pygame.font.Font("assets/fonts/AmaticSC-Regular.ttf", 36)
        self.title_text = "Labirintomaxxing"
        self.bplay_text = "Start Game"
        self.bscores_text = "Scores"
        self.startGame = False

        padding_top = 30
        padding = 30
        #botão de jogar
        self.bPlay = Button((200, 50), (self.screen_width // 2 - 100, self.screen_height // 2 + padding_top), (255, 255, 255), (200, 255, 200))
        self.bScores = Button((200, 50), (self.screen_width // 2 - 100, self.screen_height // 2 + padding_top + padding + self.bPlay.size[1]), (255, 255, 255), (200, 255, 200))

    def draw(self, screen):
        screen.fill(self.background_color)

        # Render title
        title_surface = self.title_font.render(self.title_text, True, self.text_color)
        title_rect = title_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
        screen.blit(title_surface, title_rect)

        # Detect mouse hover
        mouse_pos = pygame.mouse.get_pos()
        is_hovered_bplay = self.is_mouse_over_b_play(mouse_pos)
        is_hovered_bscores = self.is_mouse_over_b_scores(mouse_pos)
        # Escolhe a cor do botão
        b_play_color = self.b_play_color_hover if is_hovered_bplay else self.b_play_color_default
        b_scores_color = self.b_scores_color_hover if is_hovered_bscores else self.b_scores_color_default

        # Cria botão
        b_play_surface = pygame.Surface(self.b_play_size)
        b_play_surface.fill(b_play_color)

        b_scores_surface = pygame.Surface(self.b_scores_size)
        b_scores_surface.fill(b_scores_color)

        # Renderiza o texto do botão
        bplay_text_surface = self.regular_font.render(self.bplay_text, True, self.text_color)
        bplay_text_rect = bplay_text_surface.get_rect(center=(self.b_play_size[0] // 2, self.b_play_size[1] // 2))
        b_play_surface.blit(bplay_text_surface, bplay_text_rect)

        bscores_text_surface = self.regular_font.render(self.bscores_text, True, self.text_color)
        bscores_text_rect = bscores_text_surface.get_rect(center=(self.b_scores_size[0] // 2, self.b_scores_size[1] // 2))
        b_scores_surface.blit(bscores_text_surface, bscores_text_rect)

        # Desenha o botão na tela
        screen.blit(b_play_surface, self.b_play_position)
        screen.blit(b_scores_surface, self.b_scores_position)

    def update(self):
        if self.check_start_b_play_click():
            self.startGame = True

    def is_mouse_over_b_play(self, mouse_pos):
        x, y = self.b_play_position
        w, h = self.b_play_size
        return x <= mouse_pos[0] <= x + w and y <= mouse_pos[1] <= y + h

    def check_start_b_play_click(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        return self.is_mouse_over_b_play(mouse_pos) and mouse_click[0]  # Botão esquerdo

    def is_mouse_over_b_scores(self, mouse_pos):
        x, y = self.b_scores_position
        w, h = self.b_scores_size
        return x <= mouse_pos[0] <= x + w and y <= mouse_pos[1] <= y + h
    
    def check_scores_b_click(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        return self.is_mouse_over_b_scores(mouse_pos) and mouse_click[0]