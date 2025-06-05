from maze import Wall, newMaze, generateWallList, getMazeInfo
from player import Player
from screens import PauseMenu
import pygame 

class NewGame:
    def __init__ (self, SCREEN_WIDTH, SCREEN_HEIGHT, level_difficulty):
        self.classWallList = generateWallList(level_difficulty, SCREEN_WIDTH, SCREEN_HEIGHT)
        options = getMazeInfo()
        # Initialize player
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, min(options["wall_size"], options["wall_size"]) // 3)
        self.isPaused = False
        self.pauseMenu = PauseMenu(SCREEN_WIDTH, SCREEN_HEIGHT)

        
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
    
    def update(self, dt, screen, events):

        
    
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.isPaused = not self.isPaused
        #if event.key == pygame.K_r:
        # Reset player position to the center of the screen
            #self.player.move_to_cell(len(self.classWallList[0].rect) // 2, len(self.classWallList) // 2, self.classWallList[0].rect.width, self.classWallList[0].rect.height)
        # Calculate speed based on delta time

        if self.isPaused:
            self.pauseMenu.draw()
            return
    

        if dt == 0:
            dt = 1 / 60 # Prevent division by zero
        if dt > 1:
            dt = 1 / 60 # Prevent dt from being too large
        # Speed is 300 pixels per second
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