import random
import pygame

screen_w = 400
screen_h = 400
Yellow = ( 255, 255, 0 )
Black = ( 0, 0, 0 )
screen = pygame.display.set_mode( ( screen_w, screen_h ) )
### This class will store the number of coin objects in a list ###
class Coins():
    def __init__(self, num, interior_walls_pos):
        self.num = num
        self.o_list = []
        self.o_list_rect = []
        self.did_collide = []
        self.win_count = 0
        self.image = pygame.image.load("coin.png").convert()

        y = 0
        ### Use modulus to alternate the coins y-pos.
        for i in range(0, self.num):

            if i % 2 == 0:
                y = 380
            else:
                y = 10

            x = random.randrange(random.randrange(10, 20), random.randrange(340, 380))
            coin_pos = (x, y)
            self.o_list.append(pygame.Rect( coin_pos[0], coin_pos[1], 10, 10 ))
            self.o_list_rect.append(pygame.Rect( coin_pos[0], coin_pos[1], 10, 10 ))
            self.did_collide.append(False)

            """ The commented code below was my attempt at getting the coins to spawn more
            randomly across the screen. Wish to figure this out in the future.
            Possible fix: test if coin.position colides with the walls in the wall list.
            """ 
            #x = random.randrange(random.randrange(10, 20), random.randrange(340, 380))
            #y = random.randrange(random.randrange(10, 20), random.randrange(340, 380))
            """
            for wall_pos in interior_walls_pos:
                while coin_pos == wall_pos:
                    x = random.randrange(10, 380)
                    y = random.randrange(10, 380)
                    coin_pos = (x, y)
            """


    # This function will detect the coin collision with the player.
    # If the player obtains a coin, then black will be drawn in-place of the coin.
    def obj_collision(self, sq):
        i = 0
        for o in self.o_list:
            if sq.rect.colliderect(o) and not self.did_collide[i]:
                self.win_count += 1
                self.did_collide[i] = True
                pygame.draw.rect( screen, Black, o )
            i +=1

    # This function will draw the coins only if their collision value is not True.
    # If coin.did_collide is True, then the player has them; no need to re-draw.
    def update_coin_display(self):
        k = 0
        for did in self.did_collide:
            if not did:
                screen.blit(self.image, self.o_list_rect[k])
            k += 1
########################### END ###############################
