import sys
from random import choice, randint
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
DIAMOND = 4

ASSETS_PATH = './assets/'

# Link tiles to colours
TILE_TEXTURES = {
    DIRT: load(ASSETS_PATH + 'dirt.png'),
    GRASS: load(ASSETS_PATH + 'grass.png'),
    WATER: load(ASSETS_PATH + 'water.png'),
    COAL: load(ASSETS_PATH + 'coal.png'),
    DIAMOND: load(ASSETS_PATH + 'diamond.png'),
}

RESOURCES = [ DIRT, GRASS, WATER, COAL, DIAMOND ]

# Game dimensions
TILE_SIZE = 32
MAP_WIDTH = 20
MAP_HEIGHT = 20

# Generate base map
tilemap = [
    [ DIRT for w in range(MAP_WIDTH) ]
    for h in range(MAP_HEIGHT)
]

# Plot tiles
for t_row in range(MAP_HEIGHT):
    for t_column in range(MAP_WIDTH):
        rand_val = randint(0, 99)
        if rand_val == 0:
            tilemap[t_row][t_column] = DIAMOND
        elif rand_val < 5:
            tilemap[t_row][t_column] = COAL
        elif rand_val < 25:
            tilemap[t_row][t_column] = WATER
        elif rand_val < 70:
            tilemap[t_row][t_column] = GRASS

pygame.init()

# Set the width and height of the screen [width, height]
WINDOW_WIDTH = MAP_WIDTH * TILE_SIZE
WINDOW_HEIGHT = MAP_HEIGHT * TILE_SIZE
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
MAIN_WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('2D MineCraft')
clock = pygame.time.Clock()

PLAYER = load(ASSETS_PATH + 'player-01.png').convert_alpha()
player_pos = [ 0, 0 ]

inventory = {
    DIRT: 0,
    GRASS: 0,
    WATER: 0,
    COAL: 0,
    DIAMOND: 0,
}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            # Move the player with the arrow keys
            if event.key == K_RIGHT and player_pos[0] < MAP_WIDTH - 1:
                player_pos[0] += 1
            elif event.key == K_LEFT and player_pos[0] > 0:
                player_pos[0] -= 1
            elif event.key == K_DOWN and player_pos[1] < MAP_HEIGHT -1:
                player_pos[1] += 1
            elif event.key == K_UP and player_pos[1] > 0:
                player_pos[1] -= 1

            if event.key == K_SPACE:
                current_tile = tilemap[player_pos[1]][player_pos[0]]
                inventory[current_tile] += 1
                print(inventory)

    # Background colour
    MAIN_WINDOW.fill(WHITE)

    # Draw the tiles
    for row in range(MAP_HEIGHT):
        for column in range(MAP_WIDTH):
            MAIN_WINDOW.blit(
                TILE_TEXTURES[tilemap[row][column]],
                (column * TILE_SIZE, row * TILE_SIZE)
            )

    # Draw player
    MAIN_WINDOW.blit(
        PLAYER,
        ((player_pos[0] * TILE_SIZE)+8,
         (player_pos[1] * TILE_SIZE)+8)
    )

    # Refresh display
    pygame.display.flip()
    clock.tick(60)
