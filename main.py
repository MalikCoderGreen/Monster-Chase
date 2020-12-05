import pygame, sys
import random
import df_players
import math
import walls
import objs


############## Colors for Screen #############################
Black = ( 0, 0, 0 )
White = ( 255, 255, 255 )
Green = ( 0, 255, 0 )
Red = ( 255, 0, 0 )
Yellow = ( 255, 255, 0 )
Gray = ( 128, 128, 128 )
Blue = ( 42, 71, 101 )
######################## END #################################

########### intial set up; variables for screen ##############
pygame.init()
screen_w = 400
screen_h = 400
screen = pygame.display.set_mode( ( screen_w, screen_h ) )
pygame.display.set_caption('|***|MONSTER CHASE!|***|')
screen_rect = screen.get_rect()
######################### END ################################

##Create postion for user/monster and randomly spawn them ####

px =  random.randrange( 200, 350 )
py =  random.randrange( 200, 350 )


mx = random.randrange( 20, 160 )
my = random.randrange( 20, 160 )

#if (px in range(0, mx)
##This loop will keep p1 and monster from spawning too close.##


monster = df_players.DF_Monster( mx, my )
monster.draw( screen, Green )

player1 = df_players.User( px, py )
player1.draw( screen, Red )

######################### END ################################

### Create objectives for p1 to try and obtain ###############

num_of_obj = 10
num_of_walls = 3

Walls = walls.Interior_Walls(num_of_walls)
Objs = objs.Objectives(num_of_obj)

# Main loop for game; Will update users position based on input #

run = True
validMove = True # For boundary checking.

### NEWEST PROBLEM: get monster to close in on player1 x and y pos.

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # Method allows user to hold down keys.
    keys = pygame.key.get_pressed()
    player1.updateMove(keys)
    monster.findPlayer(player1.rect.left, player1.rect.top)

    Walls.wall_collision(player1, monster) # Detect if player or monster hit wall.

    # Keep player and monster on screen.
    player1.rect.clamp_ip(screen_rect)
    monster.rect.clamp_ip(screen_rect)
    screen.fill(Black)

    k = 0
    for did in Objs.did_collide:
        if not did:
            pygame.draw.rect(screen, Yellow, Objs.o_list[k])
        k += 1


    pygame.draw.rect( screen, Red, player1.rect )
    pygame.draw.rect( screen, Green, monster.rect )

    Walls.draw_walls()
    #Objs.draw_objs()

    for wall in Walls.w_list:
        wall.clamp_ip(screen_rect)
    for o in Objs.o_list:
        o.clamp_ip(screen_rect)


    # Detect if the monster has caught player 1; if so, end the game.
    if player1.rect.colliderect(monster) or monster.rect.colliderect(player1):
        print("\nGame Over! The monster got you!... =(\n")
        run = False

    # Detect if player has obtained an objective.
    Objs.obj_collision(player1)
    if Objs.win_count == num_of_obj:
        print("\nCongrats! you got all the objectives safely!\nYou Win!!\n")
        run = False


    pygame.display.flip()


######################### END ################################

###################### Collision Function ####################


pygame.quit()
