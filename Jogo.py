# Example file showing a circle moving on screen
from maze import Wall, newMaze
from player import Player
from title_screen import TitleScreen
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

game = Mode1NewGame(SCREEN_WIDTH, SCREEN_HEIGHT)
titleScreen = TitleScreen(SCREEN_WIDTH, SCREEN_HEIGHT)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # draw maze walls

    if titleScreen.startGame:
        game.update(dt, screen, clock)
    else:
        titleScreen.draw(screen)
        titleScreen.update()

    # get the time since last frame in seconds
    dt = clock.tick(60) / 1000
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()