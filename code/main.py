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
clock = pygame.time.Clock() # controls frame rate

# plain surface
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

# image imports
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha() # creates a dynamic filepath to the spaceship image
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)) # creates rect and places center of rect at (0,0)
player_direction = pygame.math.Vector2()
player_speed = 300

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)] 

meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT-20))

# event loop that checks for events such as key presses, mouse clicks, etc. and handles them accordingly
while running:
    dt = clock.tick() / 1000 # frame rate
    
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
           
       # if event.type == pygame.MOUSEMOTION:
       #     print(event.pos) 
       #     player_rect.center = event.pos   

    # input
    # print(pygame.mouse.get_rel())
    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) # sets player direction to 1 if right key is pressed, -1 if left key is pressed, and 0 if neither or both keys are pressed
    player_direction.y = int(keys[pygame.K_DOWN] - keys[pygame.K_UP]) 
    player_rect.center += player_direction * player_speed * dt
    player_direction = player_direction.normalize() if player_direction else player_direction # normalizes the player direction vector to have a magnitude of 1, but only if the vector is not zero to avoid division by zero errors
    #print(player_direction)

    recent_keys = pygame.key.get_just_pressed()
    if recent_keys[pygame.K_SPACE]:
            print("fire laser") 
            # draw the game elements here
    display_surface.fill('darkgray')
    for pos in star_positions:
        display_surface.blit(star_surf, pos) # draws the star surface at random positions on the display
    

    # draws the surface onto the display at the specified position    
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    display_surface.blit(player_surf, player_rect) 
    
    #player_rect.center += player_direction  * player_speed * dt # using vector math to move the player in a specific direction
   
    
    

    pygame.display.update() # updates the display to show any changes made to the game elements
           
pygame.quit() # uninitializes all pygame modules and is required to clean up resources when the game is closed

