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
screen_w = 600
screen_h = 600
screen = pygame.display.set_mode( ( screen_w, screen_h ) )
pygame.display.set_caption('Coin-Chaser')
game_rect = pygame.Rect(0, 0, 540, 540) # Will contain all objects aside from game boarder.

######################### END ################################

#font & string variables will be used to print info to screen#
coins_got_font = pygame.font.SysFont("impact", 20)
coins_left_font = pygame.font.SysFont("impact", 20)
you_lost_font = pygame.font.SysFont("impact", 20)
coins_gotten = ""
coins_left = ""
######################### END ################################

##Create postion for user/monster and randomly spawn them ####
px =  random.randrange( random.randrange(0,35), random.randrange(320,350) )
py =  random.randrange( 320, 350 )
mx = random.randrange( 350, 380 )
my = 10 # monster will always be somewhere at the top of the screen.

monster = df_players.DF_Monster( mx, my )
player1 = df_players.User( px, py )

######################### END ################################

########## Function: prints the game boarder to screen #######
def print_game_boarder():
    # Draw visual game boarder.
    for i in range(540):
        pygame.draw.rect(screen, Silver, (i, 560, 20, 20) ) # Bottom of screen.
        pygame.draw.rect(screen, Silver, (560, i, 20, 20) ) # Right of screen.

    pygame.draw.rect(screen, Silver, (560, 560, 20, 20) )
    return
######################### END ################################
def keep_contained(walls, coins):
    for wall in walls.w_list:
        wall.clamp_ip(game_rect)
    for o in coins.o_list:
        o.clamp_ip(game_rect)

### Create coins and interior walls for game #################
total_coins = 40
num_of_walls = 25
Walls = walls.Interior_Walls(num_of_walls)
coins_for_game = game_coins.Coins(total_coins, Walls.w_list_of_pos) #Walls.w_list_of_pos
######################### END ################################

# Main loop for game; Will update users position based on input #
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # Method allows user to hold down keys.
    keys = pygame.key.get_pressed()
    player1.update_move(keys) # apply to player1 object movements.

    # This condition ensures the monster will wait for the player's move.
    if player1.direction != "wait":
        monster.findPlayer(player1.rect.left, player1.rect.top)

    Walls.wall_collision(player1, monster, keys) # Detect if player or monster hit wall.

    # Keep player and monster within the game window (not entire screen).
    player1.rect.clamp_ip(game_rect)
    monster.rect.clamp_ip(game_rect)
    screen.fill(Black)

    print_game_boarder()

    # The method calls below will update each type of object to the screen.
    coins_for_game.update_coin_display()
    player1.draw()
    monster.draw()
    Walls.draw_walls()

    # Keep coins and walls contained in screen.
    keep_contained(Walls, coins_for_game)


    # Detect if the monster has caught player 1; if so, end the game.
    run = player1.detect_collision(monster, run)

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

    # Show coin information onto screen
    screen.blit(coins_got_blit, ( 450, 470 ))
    screen.blit(coins_left_blit, ( 0, 470 ))

    pygame.display.flip()


######################### END ################################

pygame.quit()
