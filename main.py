import sys
import pygame
from pygame.locals import *

# Define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Tile types
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

# Link tiles to colours
TILE_COLORS = {
    DIRT: BROWN,
    GRASS: GREEN,
    WATER: BLUE,
    COAL: BLACK,
}

tilemap = [
    [ GRASS, GRASS, GRASS, COAL ],
    [ GRASS, WATER, GRASS, GRASS ],
    [ WATER, WATER, WATER, GRASS ],
    [ GRASS, GRASS, GRASS, COAL ],
    [ GRASS, COAL, COAL, WATER ],
    [ GRASS, GRASS, GRASS, WATER ],
]

# Game dimensions
TILE_SIZE = 32
MAP_WIDTH = len(tilemap[0])
MAP_HEIGHT = len(tilemap)

pygame.init()

# Set the width and height of the screen [width, height]
WINDOW_WIDTH = MAP_WIDTH * TILE_SIZE
WINDOW_HEIGHT = MAP_HEIGHT * TILE_SIZE
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
MAIN_WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('2D MineCraft')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Background colour
    MAIN_WINDOW.fill(WHITE)

    # Draw the tiles
    for row in range(MAP_HEIGHT):
        for column in range(MAP_WIDTH):
            pygame.draw.rect(
                MAIN_WINDOW,
                TILE_COLORS[tilemap[row][column]],
                (column * TILE_SIZE, row * TILE_SIZE,
                TILE_SIZE, TILE_SIZE)
            )

    # Refresh display
    pygame.display.flip()
    clock.tick(60)
