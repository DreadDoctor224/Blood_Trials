from player import Player
import pygame
import os

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
FPS = 60  # Frames per second

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blood Trials")

#implementing background Music and putting it in the loop for running till quit
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets", "audios"))
audio_path = os.path.join(base_path, "background_music.mp3")
pygame.mixer.music.load(audio_path)
pygame.mixer.music.set_volume(0.8) #for volume adjustment
pygame.mixer.music.play(-1) #set on -1 so that it can loop till closed

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