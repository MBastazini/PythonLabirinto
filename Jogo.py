# Example file showing a circle moving on screen
from maze import Wall, newMaze
from player import Player
from new_game import NewGame as Mode1NewGame, userInput
import pygame


# pygame setup
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

game = Mode1NewGame(SCREEN_WIDTH, SCREEN_HEIGHT)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # draw maze walls

    speed = 300 * dt

    delta = userInput(speed)
    dx, dy = delta[0], delta[1]

    #Check for collisions with walls
    is_colliding = game.checkCollision(dx, dy)
    for wall in game.classWallList:
        wall.rect.x -= dx * (1-is_colliding[0])
        wall.rect.y -= dy * (1-is_colliding[1])

    #Draw the maze walls
    for i, wall in enumerate(game.classWallList):
        pygame.draw.rect(screen, wall.color, wall.rect)
    keys = pygame.key.get_pressed()

    # draw the player as a circle
    game.player.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()