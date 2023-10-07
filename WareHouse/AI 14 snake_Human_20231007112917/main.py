'''
This is the main file that runs the snake game.
'''
import pygame
import random
# Initialize the game
pygame.init()
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
# Define colors
white = (255, 255, 255)
green = (0, 255, 0)
# Define the snake class
class Snake:
    def __init__(self):
        self.size = 1
        self.positions = [(window_width // 2, window_height // 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
    def move(self):
        x, y = self.positions[0]
        if self.direction == "UP":
            y -= 10
        elif self.direction == "DOWN":
            y += 10
        elif self.direction == "LEFT":
            x -= 10
        elif self.direction == "RIGHT":
            x += 10
        self.positions.insert(0, (x, y))
        if len(self.positions) > self.size:
            self.positions.pop()
    def change_direction(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
    def draw(self):
        for position in self.positions:
            pygame.draw.rect(window, green, (position[0], position[1], 10, 10))
# Define the fruit class
class Fruit:
    def __init__(self):
        self.position = (random.randint(0, (window_width - 10) // 10) * 10, random.randint(0, (window_height - 10) // 10) * 10)
        self.apple_image = pygame.image.load("apple.png")
        self.banana_image = pygame.image.load("banana.png")
        self.is_banana = False
    def draw(self):
        if self.is_banana:
            window.blit(pygame.transform.scale(self.banana_image, (10, 10)), self.position)
        else:
            window.blit(pygame.transform.scale(self.apple_image, (10, 10)), self.position)
# Define the game function
def game():
    clock = pygame.time.Clock()
    snake = Snake()
    fruit = Fruit()
    score = 0
    is_game_over = False
    while not is_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    snake.change_direction("RIGHT")
        snake.move()
        if snake.positions[0] == fruit.position:
            snake.size += 1
            if fruit.is_banana:
                score += 2
            else:
                score += 1
            fruit = Fruit()
        if snake.positions[0][0] < 0 or snake.positions[0][0] >= window_width or snake.positions[0][1] < 0 or snake.positions[0][1] >= window_height:
            is_game_over = True
        for position in snake.positions[1:]:
            if position == snake.positions[0]:
                is_game_over = True
        window.fill(white)
        snake.draw()
        fruit.draw()
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render("Score: " + str(score), True, green)
        window.blit(score_text, (10, 10))
        pygame.display.update()
        clock.tick(20)
    # Game over screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        game_over_font = pygame.font.Font(None, 72)
        game_over_text = game_over_font.render("Game Over", True, green)
        window.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2, window_height // 2 - game_over_text.get_height() // 2))
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render("Score: " + str(score), True, green)
        window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, window_height // 2 + game_over_text.get_height() // 2 + 10))
        restart_text = score_font.render("Press 'R' to restart or 'Q' to quit", True, green)
        window.blit(restart_text, (window_width // 2 - restart_text.get_width() // 2, window_height // 2 + game_over_text.get_height() // 2 + score_text.get_height() + 20))
        pygame.display.update()
# Run the game
if __name__ == "__main__":
    game()