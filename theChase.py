import pygame, sys
import random
import numpy as np
import df_players
import math


############## Colors for Screen #############################
Black = ( 0, 0, 0 )
White = ( 255, 255, 255 )
Green = ( 0, 255, 0 )
Red = ( 255, 0, 0 )
Yellow = ( 255, 255, 0 )
Gray = ( 128, 128, 128 )
######################## END #################################

########### intial set up; variables for screen ##############

pygame.init()
font = pygame.font.Font( None, 100 )
screen_w = 420
screen_h = 420
screen = pygame.display.set_mode( ( screen_w, screen_h ) )
screen.fill(Black)
cells = 400
######################### END ###############################


################### variables for square agents  ############
dim = 20
gameSpeed = 20
######################### END ###############################


########### matrix grid that will represent the map #########


grid = []
for row in range(cells):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(cells):
        grid[row].append(0)  # Append a cell



for row in range(cells):
    for col in range(cells):
        pygame.draw.rect( screen, Black, ( row, col, dim, dim ) )


################# Establish border for game #################

bounds = []
for x in range(cells):

    grid[0][x] = "Wall"
    pygame.draw.rect( screen, Gray, ( 0, x, dim, dim ) )
    #bounds.append( grid[0][x] )


    grid[x][0] = "Wall"
    pygame.draw.rect( screen, Gray, ( x, 0, dim, dim ) )
    #bounds.append( grid[x][0] )


    grid[399][x] = "Wall"
    pygame.draw.rect( screen, Gray, ( 399, x, dim, dim ) )
    #bounds.append( grid[399][x] )


    grid[x][399] = "Wall"
    pygame.draw.rect( screen, Gray, ( x, 399, dim, dim ) )
    #bounds.append( grid[x][399] )




######################### END ################################


############# Create border for player and monster ###########



### Create postion for user / monster and randomly spawn them #

px = random.randrange( 20, 379 )
py = random.randrange( 20, 379 )


mx = random.randrange( 20, 379 )
my = random.randrange( 20, 379 )


## This loop will keep player1 and monster from being too close. ##
while ( ( px + 60 ) == mx and ( py + 60 ) == my ) or ( ( px - 60 ) == mx and ( py - 60 ) == my ):
    py = random.randrange( 20, 379 )

    mx = random.randrange( 20, 379 )
    my = random.randrange( 20, 379 )


monster = df_players.DF_Monster( gameSpeed, mx, my )
monster.draw( screen, Green )

player1 = df_players.User( gameSpeed, px, py )
player1.draw( screen, Red )

######################### END ################################

# Main loop for game; Will update users position based on input #

run = True
validMove = True # For boundary checking.

### NEWEST PROBLEM: Keep both P and M from going out of bounds.
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        if event.type == pygame.KEYDOWN: # For up, down, left and right.
            if event.key == pygame.K_LEFT:




                if validMove:

                    pygame.draw.rect( screen, Black, ( px, py, 20, 20 ) )
                    px -= gameSpeed
                    player1.rect.move_ip( -gameSpeed, 0 )
                    pygame.draw.rect( screen, Red, ( px, py, 20, 20 ) )


            elif event.key == pygame.K_RIGHT:

                pygame.draw.rect( screen, Black, ( px, py, 20, 20 ) )
                px += gameSpeed
                player1.rect.move_ip( gameSpeed, 0 )
                pygame.draw.rect( screen, Red, ( px, py, 20, 20 ) )


            elif event.key == pygame.K_UP:

                pygame.draw.rect( screen, Black, ( px, py, 20, 20 ) )
                py -= gameSpeed
                player1.rect.move_ip( 0, -gameSpeed )
                pygame.draw.rect( screen, Red, ( px, py, 20, 20 ) )


            elif event.key == pygame.K_DOWN:

                pygame.draw.rect( screen, Black, ( px, py, 20, 20 ) )
                py += gameSpeed
                player1.rect.move_ip( 0, gameSpeed )
                pygame.draw.rect( screen, Red, ( px, py, 20, 20 ) )

    # Detect if the monster has caught player 1; if so, end the game.
    if player1.rect.colliderect(monster) or monster.rect.colliderect(player1):
        run = False


    pygame.display.flip()

######################### END ################################

pygame.quit()
