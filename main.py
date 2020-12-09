import pygame, sys
import random
import df_players
import math
import walls
import game_coins

"""
file = open("pygame_fonts.txt", "w")
for font in pygame.font.get_fonts():
    file.write(f"{font}\n")
"""

############## Colors for game (some not used) #############################
Black = ( 0, 0, 0 )
Green = ( 0, 255, 0 )
Red = ( 255, 0, 0 )
Yellow = ( 255, 255, 0 )
Silver = ( 192, 192, 192)
######################## END #################################

########### intial set up; variables for screen ##############
pygame.init()
screen_w = 500
screen_h = 500
screen = pygame.display.set_mode( ( screen_w, screen_h ) )
pygame.display.set_caption('Coin-Chaser')
screen_rect = screen.get_rect()
game_rect = pygame.Rect(0, 0, 400, 400)

######################### END ################################

#font & string variables will be used to print info to screen#
coins_got_font = pygame.font.SysFont("impact", 15)
coins_left_font = pygame.font.SysFont("impact", 15)
you_lost_font = pygame.font.SysFont("impact", 15)
coins_gotten = ""
coins_left = ""
######################### END ################################

##Create postion for user/monster and randomly spawn them ####
px =  random.randrange( 20, 350 )
py =  random.randrange( 200, 250 )
mx = random.randrange( 20, 350 )
my = 10 # monster will always be somewhere at the top of the screen.

monster = df_players.DF_Monster( mx, my )
player1 = df_players.User( px, py )

######################### END ################################

########## Function: prints the game boarder to screen #######
def print_game_boarder():
    # Draw visual game boarder.
    for i in range(400):
        pygame.draw.rect(screen, Silver, (i, 420, 20, 20) ) # Bottom of screen.
        pygame.draw.rect(screen, Silver, (420, i, 20, 20) ) # Right of screen.

    pygame.draw.rect(screen, Silver, (420, 420, 20, 20) )
    return
######################### END ################################

### Create coins and interior walls for game #################
total_coins = 30
num_of_walls = 20
Walls = walls.Interior_Walls(num_of_walls)
coins_for_game = game_coins.Coins(total_coins, Walls.w_list_of_pos) #Walls.w_list_of_pos
######################### END ################################

# Main loop for game; Will update users position based on input #
clock = pygame.time.Clock()
timer = 5 # countdown for final result message.
dt = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # Method allows user to hold down keys.
    keys = pygame.key.get_pressed()
    player1.updateMove(keys) # apply to player1 object movements.

    # This condition ensures the monster will wait for the player's move.
    if player1.direction != "wait":
        monster.findPlayer(player1.rect.left, player1.rect.top)

    Walls.wall_collision(player1, monster, keys) # Detect if player or monster hit wall.

    # Keep player and monster on screen.
    player1.rect.clamp_ip(game_rect)
    monster.rect.clamp_ip(game_rect)
    screen.fill(Black)

    print_game_boarder()

    # This loop will draw the coins only if their collision value is not True.
    # If coin.did_collide is True, then the player has them; no need to re-draw.
    coins_for_game.update_coin_display()


    player1.draw()
    monster.draw()
    Walls.draw_walls()

    # Keep coins and walls contained in screen.
    for wall in Walls.w_list:
        wall.clamp_ip(screen_rect)
    for o in coins_for_game.o_list:
        o.clamp_ip(screen_rect)


    # Detect if the monster has caught player 1; if so, end the game.
    if player1.rect.colliderect(monster) or monster.rect.colliderect(player1):
        print("\nGame Over! The monster got you!... =(\n")
        #you_lost_blit = you_lost_font.render("Monster got ya! U LOSE! =(", 0, ( 255, 255, 0) )
        #screen.blit(you_lost_blit, (200, 440))
        #pygame.time.wait(8000)
        run = False


    # Detect if player has obtained a coin.
    coins_for_game.obj_collision(player1)

    # Below are text messages that will be shown to screen for user to see coin information.
    coins_gotten = f"coins: x{str(coins_for_game.win_count)}" # f-string formattiing.
    coins_left = f"coins left: {str(total_coins - coins_for_game.win_count)}"

    coins_got_blit = coins_got_font.render(coins_gotten, 0, ( 255, 255, 0) )
    coins_left_blit = coins_left_font.render(coins_left, 0, ( 255, 255, 0) )

    if coins_for_game.win_count == total_coins:
        print("\nCongrats! you got all the coins safely!\nYou Win!!\n")
        #pygame.time.delay(2000)
        run = False


    screen.blit(coins_got_blit, ( 440, 440 ))
    screen.blit(coins_left_blit, ( 0, 440 ))

    pygame.display.flip()


######################### END ################################

pygame.quit()
