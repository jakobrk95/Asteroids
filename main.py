import pygame
from constants import *

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

if __name__ == "__main__":
    main()

