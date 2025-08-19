import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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

    # Create groups to manage multiple game objects at once
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add all instances of a player object to both groups
    Player.containers = (updatable, drawable)
    # Do the same for other objects, using their relevant groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create a player object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Create the asteroid field object
    asteroid_field = AsteroidField()

    # Game loop, the for loop at the start allows one to quit the game easily
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        # Fill the entire game screen with a black surface
        screen.fill("black")

        # Update all objects that are updatable
        updatable.update(dt)

        # Draw all of the drawable objects one at a time
        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            # Check if the player is colliding with an asteroid
            if asteroid.is_colliding(player):
                sys.exit("Game Over!")
        
            # Check if any shots are colliding with an asteroid
            for shot in shots:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    asteroid.split()


        pygame.display.flip()

        # Calling .tick(60) limits the fps to 60, delta time is captured in dt
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
