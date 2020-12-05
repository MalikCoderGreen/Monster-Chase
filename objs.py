import random
import pygame

screen_w = 400
screen_h = 400
Yellow = ( 255, 255, 0 )
Black = ( 0, 0, 0 )
screen = pygame.display.set_mode( ( screen_w, screen_h ) )

class Objectives():
    def __init__(self, num):
        self.num = num
        self.o_list = []
        self.did_collide = []
        self.win_count = 0
        y = 0

        for i in range(0, self.num):
            x = random.randrange(10, 380)
            if i % 2 == 0:
                y = 380
            else:
                y = 10
            self.o_list.append( pygame.Rect( x, y, 10, 10 ) )
            self.did_collide.append(False)



    def obj_collision(self, sq):
        i = 0
        for o in self.o_list:
            if sq.rect.colliderect(o) and not self.did_collide[i]:
                self.win_count += 1
                self.did_collide[i] = True
                pygame.draw.rect( screen, Black, o )
            i +=1
