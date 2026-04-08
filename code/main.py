import pygame
from os.path import join # makes filepaths dynamic for different operation systems
from random import randint

# general setup

pygame.init()  # initializes pygame and is required before using any other pygame functions

# Sets screen dimensions
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption('Space Shooter')
running = True

# plain surface
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

# importing an image

player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha() # creates a dynamic filepath to the image
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)] 


# event loop that checks for events such as key presses, mouse clicks, etc. and handles them accordingly
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

            # draw the game elements here
    display_surface.fill('darkgray')
    for pos in star_positions:
        display_surface.blit(star_surf, pos) # draws the star surface at random positions on the display

    x += 0.1
    display_surface.blit(player_surf, (x,150)) # draws the surface onto the display at the specified position
    pygame.display.update() # updates the display to show any changes made to the game elements
           
pygame.quit() # uninitializes all pygame modules and is required to clean up resources when the game is closed

