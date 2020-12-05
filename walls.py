import random
import pygame

Blue = ( 42, 71, 101 )
screen_w = 400
screen_h = 400
screen = pygame.display.set_mode( ( screen_w, screen_h ) )

class Interior_Walls():
    def __init__(self, num):
        self.w_list = []
        self.num = num
        for i in range(0, self.num):
            dec = random.randrange(2, 20)
            x = random.randrange(30, 300)
            y = random.randrange(30, 300)
            self.w_list.append( pygame.Rect( x, y, 100, 30 ) )

    def draw_walls(self):
        for i in range(0, self.num):
            pygame.draw.rect(screen, Blue, self.w_list[i])

    def wall_collision(self, sq1, sq2):
        for wall in self.w_list:
            if sq1.rect.colliderect(wall):
                if sq1.direction == "up":
                    sq1.rect.top += sq1.speed

                if sq1.direction == "down":
                    sq1.rect.top -= sq1.speed

                if sq1.direction == "left":
                    sq1.rect.top += sq1.speed

                if sq1.direction == "right":
                    sq1.rect.top -= sq1.speed

            if sq2.rect.colliderect(wall):
                if sq2.direction == "up":
                    sq2.rect.top += sq2.speed

                if sq2.direction == "down":
                    sq2.rect.top -= sq2.speed

                if sq2.direction == "left":
                    sq2.rect.top += sq2.speed

                if sq2.direction == "right":
                    sq2.rect.top -= sq2.speed
