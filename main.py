import sys
import pygame
from pygame.image import load
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

ASSETS_PASTH = './assets/'

# Link tiles to colours
TILE_TEXTURES = {
    DIRT: load(ASSETS_PASTH + 'dirt.png'),
    GRASS: load(ASSETS_PASTH + 'grass.png'),
    WATER: load(ASSETS_PASTH + 'water.png'),
    COAL: load(ASSETS_PASTH + 'coal.png'),
}

tilemap = [
    [ DIRT, GRASS, GRASS, COAL ],
    [ DIRT, WATER, GRASS, GRASS ],
    [ WATER, WATER, WATER, GRASS ],
    [ GRASS, GRASS, GRASS, COAL ],
    [ GRASS, COAL, COAL, WATER ],
    [ DIRT, GRASS, GRASS, WATER ],
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
            MAIN_WINDOW.blit(
                TILE_TEXTURES[tilemap[row][column]],
                (column * TILE_SIZE, row * TILE_SIZE)
            )

    # Refresh display
    pygame.display.flip()
    clock.tick(60)
