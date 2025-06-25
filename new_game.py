from maze import Wall, newMaze, generateWallList, getMazeInfo
import settings
from player import Player
from screens import PauseMenu
from util import TextBox
import pygame 

SPEED = 501 # Speed in pixels per second

pygame.time.set_timer(pygame.USEREVENT, 100)

class NewGame:
    def __init__ (self, SCREEN_WIDTH, SCREEN_HEIGHT, level_difficulty=1, DEBUG_MODE=False, custom_maze=None):

        matrix = None
        if(custom_maze):
            level_path = settings.level_path + custom_maze + ".txt"
            string = open_file(level_path)
            matrix = create_matrix(string)
            print(f"Loading level {custom_maze} from {level_path}...")
            
            if not matrix:
                print(f"Error: Level {custom_maze} not found or empty.")
                self.nextScreen = 'title'
                return
        else:
            matrix = newMaze(23 + (
                level_difficulty * 4 * 3
            )) #multiplos de 4 (o 3 é a escala com que as dificuldades aumentam)

        self.classWallList = generateWallList(SCREEN_WIDTH, SCREEN_HEIGHT, DEBUG_MODE, matrix)
        self.options = getMazeInfo()
        # Initialize player

        self.nextScreen = None 
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, self.options["wall_size"] // 3)
        self.pauseMenu = PauseMenu(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.speed = SPEED * self.options["wall_size"] / 100  # Adjust speed based on wall size

        self.exit_rect = [wall.rect for wall in self.classWallList if wall.type == "exit"][0]  # Get the exit wall rectangle

        self.bonus_squares = [wall.rect for wall in self.classWallList if wall.type == "bonus"]  # Get all bonus squares

        self.time_display = TextBox(
            position=(SCREEN_WIDTH - 150, 10), 
            size=(140, 30), 
            text_color=(0, 0, 0), 
            background_color=(126, 217, 81),
            font=1,
            text="Time: 0.00s"
        )

        self.debug_mode = DEBUG_MODE
        self.current_seconds = 0

        self.is_level = True if custom_maze else False  # Determine if this is a level or a custom maze
        self.level = None if not custom_maze else custom_maze
        self.matrix = matrix if matrix else None  # Store the matrix if provided, otherwise None

    def checkCollision(self, dx, dy):
        is_colliding = [False, False] #Eixo X e Y
        # Check for collisions with walls
        playerPosHitbox = self.player.hitbox.copy()
        playerPosHitbox_x = playerPosHitbox.move(dx, 0)
        playerPosHitbox_y = playerPosHitbox.move(0, dy)
        #paint the new hitbox
        if self.debug_mode:
            pygame.draw.rect(pygame.display.get_surface(), "blue", playerPosHitbox_x, 2)
            pygame.draw.rect(pygame.display.get_surface(), "yellow", playerPosHitbox_y, 2)


        mazeHitbox = [wall.rect for wall in self.classWallList if wall.active]  # Only check active walls
        is_colliding[0] = playerPosHitbox_x.collidelist(mazeHitbox) != -1
        is_colliding[1] = playerPosHitbox_y.collidelist(mazeHitbox) != -1
        return is_colliding
    
    def checkBonusCollision(self):
        """
        Check if the player collides with any bonus squares.
        If a collision occurs, return True and remove the bonus square from the list.
        """
        for bonus in self.bonus_squares:
            if self.player.hitbox.colliderect(bonus):
                self.bonus_squares.remove(bonus)
                self.player.bonusSquare()  # Increment player points

    def update(self, dt, screen, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pauseMenu.isPaused = not self.pauseMenu.isPaused
                 #if event.key == pygame.K_r:
                    # Reset player position to the center of the screen
                    #self.player.move_to_cell(len(self.classWallList[0].rect) // 2, len(self.classWallList) // 2, self.classWallList[0].rect.width, self.classWallList[0].rect.height)
            if event.type == pygame.USEREVENT and not self.pauseMenu.isPaused:
                self.current_seconds += 0.1

        if not self.pauseMenu.isPaused:
            if dt == 0:
                dt = 1 / 60 # Prevent division by zero
            if dt > 1:
                dt = 1 / 60 # Prevent dt from being too large
            # Speed is 300 pixels per second
            speed = self.speed * dt

            delta = userInput(speed)
            dx, dy = delta[0], delta[1]

            #Check for collisions with walls
            is_colliding = self.checkCollision(dx, dy)
            for wall in self.classWallList:
                wall.rect.x -= dx * (1-is_colliding[0])
                wall.rect.y -= dy * (1-is_colliding[1])
            
            if (self.player.hitbox.colliderect(self.exit_rect)):
                self.nextScreen = 'win'

            self.checkBonusCollision()

        #Draw the maze walls
        for i, wall in enumerate(self.classWallList):
            pygame.draw.rect(screen, wall.color, wall.rect)
        keys = pygame.key.get_pressed()

        # draw the player as a circle
        self.player.draw(screen, self.debug_mode)

        self.time_display.draw(screen, text=f"Time: {self.current_seconds:.1f}s")

        if self.pauseMenu.isPaused:
            self.pauseMenu.draw(screen)
            events = self.pauseMenu.update(screen, events)
            #events is a dictionary, shows all the items inside:
            if "return_to_menu" in events:
                self.nextScreen = 'title'
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


def open_file(file_path):
    try:
        with open(file_path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def create_matrix(string):
    new_matrix = []
    for linha in string.split("\n"):
        if linha.strip() == "":
            continue
        new_matrix.append([char for char in linha.strip()])
    return new_matrix