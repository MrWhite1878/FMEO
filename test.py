import pygame

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)

# Set up the game window
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Resizable Pygame Window")

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Update the window size to be a square
            size = min(event.size)
            WINDOW_SIZE = (size, size)
            screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)

    # Draw the screen
    screen.fill(BLACK)
    pygame.display.flip()

# Quit Pygame
pygame.quit()