from util import Button, TextBox, BackButton
import pygame
import settings
import ast
import string

class CampaignScreen:
    def __init__(self, screen_width, screen_height):
        # --- Configurações Iniciais ---
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = (126, 217, 81)
        self.text_color = (28, 77, 5)
        self.next_screen = None
        self.level_buttons = []

        # --- Componentes de UI ---
        self.title = TextBox(
            position=(self.screen_width // 2 - 200, 50),
            size=(400, 100), text="Campaign", font=2,
            text_color=self.text_color, background_color=False
        )
        self.back_button = BackButton(onClick=self.back_to_level_selector)

        # --- Lógica de Inicialização ---
        # 1. Determina o número total de fases a partir do cache
        try:
            with open("saves/fases/cache.txt", "r") as cache_file:
                self.level_count = int(cache_file.readline().strip())
        except (FileNotFoundError, ValueError):
            self.level_count = 0
        
        # 2. Prepara a lista de progresso (inicialmente todos como não concluídos)
        self.level_completed = [False] * self.level_count

        # 3. Carrega o progresso salvo do jogador (nova função)
        self._carregar_progresso()

        # 4. Cria os botões na tela com base no progresso carregado
        self.cria_botoes_init()

    def _carregar_progresso(self):
        """Lê o arquivo de save e preenche a lista self.level_completed."""
        try:
            path = settings.saves_path[settings.active_save_file - 1]
            with open(path, "r") as save_file:
                # Usando enumerate para obter o índice e a linha de forma mais elegante
                for i, line in enumerate(save_file):
                    # Garante que não tentemos acessar um índice fora dos limites
                    if i >= self.level_count:
                        break
                    
                    line = line.strip()
                    if not line:
                        continue
                        
                    try:
                        object = ast.literal_eval(line)
                        if 'is_level' in object:
                            if 'level' in object and object['level'] is not None:
                                self.level_completed[int(object['level'].replace("fase",""))-1] = object['is_level']
                    except (ValueError, SyntaxError, KeyError):
                        print(f"Error parsing line {i+1} in save file: {line}")
                        # Mantém o valor como False se a linha for malformada
                        self.level_completed[i] = False

        except FileNotFoundError:
            print(f"Save file not found. Starting with no levels completed.")
            # Se o arquivo não existe, a lista self.level_completed (cheia de False) já está correta.
        except IndexError:
            print("Error: Active save file setting is invalid.")
            # Lida com o caso de settings.active_save_file estar fora do alcance do array.


    def cria_botoes_init(self):
        """Cria e posiciona os botões de seleção de nível."""
        total_button_width = 50 * 4 + 50 * 3
        initial_padding = (self.screen_width - total_button_width) // 2
        
        count = 1
        for i in range(4):  # Linhas
            for j in range(4):  # Colunas
                if count > self.level_count: break
                
                pos_x = initial_padding + (100 * j)
                pos_y = (self.screen_height // 2 - 100) + (100 * i)
                button_color = (51, 204, 51) if self.level_completed[count - 1] else (255, 255, 255)

                newBtn = Button(
                    text=f"{count}", size=(50, 50), position=(pos_x, pos_y),
                    onClick=lambda level=count: self.select_level(level),
                    color=button_color
                )
                self.level_buttons.append(newBtn)
                count += 1
            if count > self.level_count: break

    
    def recarregar_botoes(self):
        self._carregar_progresso()
        self.level_buttons.clear()
        self.cria_botoes_init()

    def select_level(self, level):
        self.next_screen = f"fase{level}"

    def back_to_level_selector(self):
        self.next_screen = "level_selector"

    def draw(self, screen):
        screen.fill(self.background_color)
        self.title.draw(screen)
        self.back_button.draw(screen)
        for button in self.level_buttons:
            button.draw(screen)

    def update(self, screen, events):
        for button in self.level_buttons:
            button.update(events)
        self.back_button.update(events)
        self.draw(screen)