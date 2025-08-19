import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame and set window resolution
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock to limit the game to 60 fps and decouple game speed from computer speed
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Game loop, the for loop at the start allows one to quit the game easily
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        pygame.Surface.fill(screen, "black")

        player.draw(screen)
        player.update(dt)

        pygame.display.flip()

        # Calling .tick(60) limits the fps to 60, delta time is captured in dt
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
