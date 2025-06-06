# Example file showing a circle moving on screen
from maze import Wall, newMaze
from player import Player
from screens import TitleScreen, LevelSelector
from new_game import NewGame as Mode1NewGame, userInput
import pygame


# pygame setup
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

game = None  # Initialize game variable
titleScreen = TitleScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
levelSelector = LevelSelector(SCREEN_WIDTH, SCREEN_HEIGHT)

activeScreen = "title"  # Track which screen is active
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
        case "title":
            titleScreen.update(screen, events)
            if titleScreen.startGame:
                activeScreen = "level_selector"
                titleScreen.startGame = False
        case "level_selector":
            levelSelector.update(screen, events)
            if levelSelector.startGame:
                game = Mode1NewGame(SCREEN_WIDTH, SCREEN_HEIGHT, levelSelector.difficulty)
                activeScreen = "game"
                levelSelector.startGame = False
        case "game":
            game.update(dt, screen, events)
            if not game.active:
                activeScreen = "title"
                del game
            #if pygame.key.get_pressed()[pygame.K_ESCAPE]:  # Press ESC to return to title screen
            #    activeScreen = "title"

    # get the time since last frame in seconds
    dt = clock.tick(60) / 1000
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()