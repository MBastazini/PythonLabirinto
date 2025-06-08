import pygame

# pygame setup
pygame.init()

# Example file showing a circle moving on screen
from maze import Wall, newMaze
from player import Player
from screens import TitleScreen, LevelSelectorScreen, ScoresScreen, WinScreen, CampaignScreen, NewLevelScreen
from screens import NewPlayerScreen
from new_game import NewGame as Mode1NewGame, userInput


DEBUG_MODE = False

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

game = None  # Initialize game variable
titleScreen = None
levelSelector = LevelSelectorScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
campaignScreen = CampaignScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
newLevelScreen = NewLevelScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
newPlayerScreen = NewPlayerScreen(SCREEN_WIDTH, SCREEN_HEIGHT)

scoresScreen = ScoresScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
winScreen = None
activeScreen = "title"  # Track which screen is active

player_file = None
try:
    player_file = open("saves/players/player_2.txt", "r")
    titleScreen = TitleScreen(SCREEN_WIDTH, SCREEN_HEIGHT, player_file)
except FileNotFoundError:
    activeScreen = "new_player"

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
        case "new_player":
            newPlayerScreen.update(screen, events)
            if newPlayerScreen.next_screen:
                activeScreen = newPlayerScreen.next_screen
                newPlayerScreen.next_screen = None
                if activeScreen == "title":
                    titleScreen = TitleScreen(SCREEN_WIDTH, SCREEN_HEIGHT, player_file)
        case "title":
            if(titleScreen):
                titleScreen.update(screen, events)
                if titleScreen.nextScreen:
                    activeScreen = titleScreen.nextScreen
                    titleScreen.nextScreen = None
            else:
                # If player file is not found, show new player screen
                activeScreen = "new_player"
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
        case "game":
            game.update(dt, screen, events)
            if game.nextScreen:
                activeScreen = game.nextScreen
                elapsed_time = game.current_seconds
                game = None
                if( activeScreen == "win"):
                    winScreen = WinScreen(SCREEN_WIDTH, SCREEN_HEIGHT, elapsed_time)
        case "win":
            winScreen.update(screen, events)
            if winScreen.next_screen:
                activeScreen = winScreen.next_screen
                winScreen = None
            #if pygame.key.get_pressed()[pygame.K_ESCAPE]:  # Press ESC to return to title screen
            #    activeScreen = "title"

    # get the time since last frame in seconds
    dt = clock.tick(60) / 1000
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()