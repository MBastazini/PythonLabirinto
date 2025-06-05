from maze import Wall, newMaze
from player import Player
import pygame 

class NewGame:
    def __init__ (self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.matriz = newMaze(21)

        self.classWallList = []
        WALL_SIZE = 100  # Tamanho do bloco da parede
        # draw walls based on the matrix
        #Tamanho usando ocupando a tela inteira
        #wall_width = SCREEN_WIDTH // len(matriz[0])
        #wall_height = SCREEN_HEIGHT // len(matriz)
        wall_width = WALL_SIZE
        wall_height = WALL_SIZE
        for y, row in enumerate(self.matriz):
            for x, cell in enumerate(row):
                if cell == 1:
                    wall = Wall(x * wall_width, y * wall_height, wall_width, wall_height)
                    self.classWallList.append(wall)
                if cell == 2:
                    # If the cell is the starting point, draw it as a wall
                    wall = Wall(x * wall_width, y * wall_height, wall_width, wall_height, color="green", active=False)
                    self.classWallList.append(wall)

        # Initialize player
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, min(wall_width, wall_height) // 3)

        for wall in self.classWallList:
            wall.rect.x -= (WALL_SIZE * len(self.matriz[0])) // 2 - SCREEN_WIDTH // 2
            wall.rect.y -= (WALL_SIZE * len(self.matriz)) // 2 - SCREEN_HEIGHT // 2
    def checkCollision(self, dx, dy):
        is_colliding = [False, False] #Eixo X e Y
        # Check for collisions with walls
        playerPosHitbox = self.player.hitbox.copy()
        playerPosHitbox_x = playerPosHitbox.move(dx, 0)
        playerPosHitbox_y = playerPosHitbox.move(0, dy)
        mazeHitbox = [wall.rect for wall in self.classWallList if wall.active]  # Only check active walls
        is_colliding[0] = playerPosHitbox_x.collidelist(mazeHitbox) != -1
        is_colliding[1] = playerPosHitbox_y.collidelist(mazeHitbox) != -1
        return is_colliding
    def update(self, dt, screen, clock):
        speed = 300 * dt

        delta = userInput(speed)
        dx, dy = delta[0], delta[1]

        #Check for collisions with walls
        is_colliding = self.checkCollision(dx, dy)
        for wall in self.classWallList:
            wall.rect.x -= dx * (1-is_colliding[0])
            wall.rect.y -= dy * (1-is_colliding[1])

        #Draw the maze walls
        for i, wall in enumerate(self.classWallList):
            pygame.draw.rect(screen, wall.color, wall.rect)
        keys = pygame.key.get_pressed()

        # draw the player as a circle
        self.player.draw(screen)

def userInput(speed=1):
    """
    Function to handle user input for moving the player.
    Returns a tuple of (dx, dy) representing the movement direction.
    """
    keys = pygame.key.get_pressed()
    dx = 0
    dy = 0
    if keys[pygame.K_w]:
        dy = -1 * speed
    if keys[pygame.K_s]:
        dy = 1 * speed
    if keys[pygame.K_a]:
        dx = -1 * speed
    if keys[pygame.K_d]:
        dx = 1 * speed  
    return [dx, dy]