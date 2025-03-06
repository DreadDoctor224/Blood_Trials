from player import Player
import pygame

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
FPS = 60  # Frames per second

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blood Trials")

# Create player object
player = Player(WIDTH//2, HEIGHT - 100)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)
    player.attack(keys)  # Handle attack
    player.update()  # Update attack state

    screen.fill((0, 0, 0))  # Clear the screen (black background)
    player.draw(screen)  # Draw player

    pygame.display.update()
    clock.tick(FPS)  # Limit FPS

pygame.quit()