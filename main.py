import pygame
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"""
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}
    """)
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



    while True:
        log_state()
        # makes close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)
        
        # fills the screen with black
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)
        


if __name__ == "__main__":
    main()
