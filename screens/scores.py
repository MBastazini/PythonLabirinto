import pygame
from util import TextBox, Button, BackButton
import settings, ast

class ScoresScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = (126, 217, 81)

        self.next_screen = None 

        # --- Variáveis de Scroll ---
        self.scroll_y = 0  # NOVO: Deslocamento vertical inicial
        self.scroll_speed = 30  # NOVO: Velocidade da rolagem
        self.min_scroll_y = 0 # NOVO: Limite máximo de rolagem para baixo

        self.scores_list = []
        self.scores_texts = []


        self.back_button = BackButton(
            onClick=lambda: setattr(self, 'next_screen', 'title')
        )

        # Título da tela (sem alterações)
        self.title_box = TextBox(
            position=(screen_width // 2 - 100, 50),
            size=(200, 100),
            text="Scores",
            text_color=(0, 0, 0),
            background_color=(255, 255, 255),
            font=2
        )
        
        self._carregar_progresso()  # Carrega os scores do arquivo

        # Cria os TextBoxes para cada score
        start_y = 170 # Posição Y inicial para o primeiro score
        for i, score_data in enumerate(self.scores_list):
            # Valida se os dados do score existem
            score_value = score_data.get('coins', 0) # Usa .get() para segurança
            time_value = score_data.get('time', 0.0)

            score_text = f"{(score_data['level'].replace("fase", "Fase ") if score_data['level'] is not None else " -Custom- ") + ' | '}: {score_value} coins, Time: {time_value:.1f}s"
            score_text_box = TextBox(
                position=(screen_width // 2 - 200, start_y + i * 60), # Aumentei o espaçamento para 60
                size=(400, 50), # Aumentei a largura para caber o texto
                text=score_text,
                text_color=(28, 77, 5),
                background_color=(255, 255, 255, 180), # NOVO: Fundo com transparência
                font=1
            )
            self.scores_texts.append(score_text_box)
        
        self._calcular_limites_scroll() # NOVO: Calcula o limite de rolagem após criar os textos

    # NOVO: Função para calcular os limites da rolagem
    def _calcular_limites_scroll(self):
        """Calcula o valor mínimo que o scroll_y pode atingir."""
        if not self.scores_texts:
            return

        # Encontra a borda inferior do último item da lista
        content_bottom = self.scores_texts[-1].get_rect().bottom
        
        # Se o conteúdo já cabe na tela, não precisa rolar.
        if content_bottom < self.screen_height:
            self.min_scroll_y = 0
        else:
            # O limite é a altura da tela menos a borda inferior do conteúdo.
            # Isso garante que o último item não suba além da base da tela.
            self.min_scroll_y = self.screen_height - content_bottom - 20 # Deixa uma margem de 20px

    def draw(self, screen):
        screen.fill(self.background_color)
        self.back_button.draw(screen)  # Desenha o botão de voltar
        # Desenha cada caixa de texto de score com o deslocamento do scroll
        for score_text in self.scores_texts:
            # NOVO: Para desenhar com scroll, precisamos de uma forma de aplicar o offset.
            # A forma mais limpa é modificar o draw da sua classe TextBox para aceitar um offset,
            # mas se não for possível, podemos fazer a renderização manualmente aqui.
            
            # --- Início da Lógica de Desenho com Scroll ---
            # 1. Cria um retângulo temporário com a posição deslocada
            temp_rect = score_text.get_rect().copy()
            temp_rect.y += self.scroll_y

            # 2. Só desenha o item se ele estiver visível na tela
            if temp_rect.bottom > self.title_box.get_rect().bottom and temp_rect.top < self.screen_height:
                 # Assumindo que sua classe TextBox tem atributos 'text_surface', 'background_color' e 'rect'
                 # e que o fundo pode ter transparência
                if score_text.background_color:
                    # Cria uma surface temporária para o fundo para poder aplicar transparência
                    bg_surface = pygame.Surface(temp_rect.size, pygame.SRCALPHA)
                    bg_surface.fill(score_text.background_color)
                    screen.blit(bg_surface, temp_rect.topleft)

                screen.blit(score_text.get_text_surface(), temp_rect.topleft)
            # --- Fim da Lógica de Desenho com Scroll ---

        self.title_box.draw(screen) # O título fica fixo

    def update(self, screen, events):
        # NOVO: Lógica para processar eventos de scroll
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # event.button == 4 é o scroll para cima
                if event.button == 4:
                    self.scroll_y += self.scroll_speed
                # event.button == 5 é o scroll para baixo
                elif event.button == 5:
                    self.scroll_y -= self.scroll_speed

        # NOVO: Aplica os limites de rolagem
        # Garante que não rolemos para cima além do primeiro item (scroll_y não pode ser > 0)
        self.scroll_y = min(0, self.scroll_y)
        # Garante que não rolemos para baixo além do último item
        self.scroll_y = max(self.min_scroll_y, self.scroll_y)

        self.back_button.update(events)  # Atualiza o botão de voltar

        self.draw(screen)

    def _carregar_progresso(self):
        """Lê o arquivo de save e preenche a lista de scores."""
        try:
            path = settings.saves_path[settings.active_save_file - 1]
            with open(path, "r") as save_file:
                for i, line in enumerate(save_file):
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        obj = ast.literal_eval(line)
                        # Adiciona apenas se for um dicionário (evita adicionar 'True' ou outros tipos)
                        if isinstance(obj, dict):
                            self.scores_list.append(obj)
                    except (ValueError, SyntaxError, KeyError):
                        print(f"Error parsing line {i+1} in save file: {line}")
        except FileNotFoundError:
            print(f"Save file not found. No scores to display.")
        except IndexError:
            print("Error: Active save file setting is invalid.")