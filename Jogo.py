import pygame
import settings
import os, sys
# pygame setup
pygame.init()

# Example file showing a circle moving on screen
from maze import Wall, newMaze
from player import Player
from screens import TitleScreen, LevelSelectorScreen, ScoresScreen, WinScreen, CampaignScreen, NewLevelScreen
from screens import NewPlayerScreen, SaveFilesScreen
from new_game import NewGame as Mode1NewGame, userInput


DEBUG_MODE = True

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0




#see if the 3 save files exist, if not, create one.
def check_save_file(file_path, index):
    try:
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w") as f:
                f.write("0\n")
        else:
            with open(file_path, "r") as f:
                file = f.readlines()
            if len(file) > 0 and int(file[0]) > 0:
                settings.save_files[index][0] = True
                settings.save_files[index][1] = file[1].strip().replace("\n", "")
    except Exception as e:
        print(f"Erro ao acessar o arquivo {file_path}: {e}")
        # aqui você pode decidir o que fazer em caso de erro

check_save_file(settings.save_files[0][2], 0)
check_save_file(settings.save_files[1][2], 1)
check_save_file(settings.save_files[2][2], 2)

#checking cache file (stores the last save file used)
cache_file_path = "saves/cache.txt"
if os.path.exists(cache_file_path):
    with open(cache_file_path, "r") as f:
        try:
            settings.active_save_file = int(f.read().strip())
        except ValueError:
            settings.active_save_file = 1  # Default to first save file if cache is invalid

game = None  # Initialize game variable
titleScreen = None
levelSelector = LevelSelectorScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
campaignScreen = CampaignScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
newLevelScreen = NewLevelScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
saveFilesScreen = None
newPlayerScreen = NewPlayerScreen(SCREEN_WIDTH, SCREEN_HEIGHT, settings.save_files[settings.active_save_file - 1][2], settings.active_save_file)
scoresScreen = ScoresScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
winScreen = None
activeScreen = "title"  # Track which screen is active


#check if save_file_1 has data inside, if not, create a new player.
if (settings.save_files[settings.active_save_file - 1][0] == False):
    print(f"No player found in save file {settings.active_save_file}, creating a new player.")
    activeScreen = "first_run"
else:
    print(f"Player found in save file {settings.active_save_file}, loading the game.")
    titleScreen = TitleScreen(SCREEN_WIDTH, SCREEN_HEIGHT)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    match activeScreen:
        case "first_run":
            newPlayerScreen.update(screen, events)
            if newPlayerScreen.next_screen:
                activeScreen = newPlayerScreen.next_screen
                newPlayerScreen = None
                if activeScreen == "title":
                    titleScreen = TitleScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
        case "title":
            if(titleScreen):
                titleScreen.update(screen, events)
                if titleScreen.nextScreen:
                    if titleScreen.nextScreen == "save_files":
                        saveFilesScreen = SaveFilesScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
                    activeScreen = titleScreen.nextScreen
                    titleScreen.nextScreen = None
            else:
                # If player file is not found, show new player screen
                activeScreen = "first_run"
        case "level_selector":
            levelSelector.update(screen, events)
            if levelSelector.next_screen:
                activeScreen = levelSelector.next_screen
                levelSelector.next_screen = None
        case "campaign":
            campaignScreen.update(screen, events)
            if campaignScreen.next_screen:
                activeScreen = campaignScreen.next_screen
                campaignScreen.next_screen = None
                if activeScreen.startswith("fase"):
                    game = Mode1NewGame(SCREEN_WIDTH, SCREEN_HEIGHT, 1, DEBUG_MODE, activeScreen)
                    activeScreen = "game"

        case "save_files":
            saveFilesScreen.update(screen, events)
            if saveFilesScreen.next_screen:
                if saveFilesScreen.next_screen == "title":
                    titleScreen.reload_screen()
                if saveFilesScreen.next_screen == "new_player":
                    file_path = settings.save_files[settings.active_save_file - 1][2]
                    newPlayerScreen.change_file_path(file_path)
                activeScreen = saveFilesScreen.next_screen
                saveFilesScreen = None

        case "new_player":
            newPlayerScreen.update(screen, events)
            if (newPlayerScreen.next_screen):
                if newPlayerScreen.next_screen == "title":
                    titleScreen.reload_screen()
                activeScreen = newPlayerScreen.next_screen
                newPlayerScreen.next_screen = None
        case "new_level":
            newLevelScreen.update(screen, events)
            if newLevelScreen.next_screen:
                activeScreen = newLevelScreen.next_screen
                newLevelScreen.next_screen = None
            if newLevelScreen.startGame:
                activeScreen = "game"
                game = Mode1NewGame(SCREEN_WIDTH, SCREEN_HEIGHT, newLevelScreen.difficulty, DEBUG_MODE)
                newLevelScreen.startGame = False
        case "scores":
            scoresScreen.update(screen, events)
            if scoresScreen.next_screen:
                activeScreen = scoresScreen.next_screen
                scoresScreen.next_screen = None
        case "game":
            game.update(dt, screen, events)
            if game.nextScreen:
                activeScreen = game.nextScreen
                elapsed_time = game.current_seconds
                player_score = game.player.points

                is_level = game.is_level
                level = game.level
                matrix = game.matrix

                if(is_level):
                    matrix = level

                game = None
                if(activeScreen == "win"):
                    winScreen = WinScreen(SCREEN_WIDTH, SCREEN_HEIGHT, elapsed_time, player_score, matrix)
        case "win":
            winScreen.update(screen, events)
            if winScreen.next_screen:
                activeScreen = winScreen.next_screen
                winScreen = None
                if(activeScreen != "quit"): #TELA DE QUIT NN EXISTE AINDA
                    campaignScreen.recarregar_botoes()
        case "reload":
            #reload this entire file
            print("Reloading game...")
            os.execv(sys.executable, ['python'] + sys.argv)

            #if pygame.key.get_pressed()[pygame.K_ESCAPE]:  # Press ESC to return to title screen
            #    activeScreen = "title"

    # get the time since last frame in seconds
    dt = clock.tick(60) / 1000
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()