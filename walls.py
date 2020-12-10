import random
import pygame

Blue = ( 30, 144, 255 )
screen_w = 400
screen_h = 400
screen = pygame.display.set_mode( ( screen_w, screen_h ) )
### This class will store the number of interior walls in a list ###
class Interior_Walls():
    def __init__(self, num):
        self.w_list = []
        self.num = num
        self.w_list_of_pos = []
        self.image_horizontal = pygame.image.load("brick_texture.png").convert()
        self.image_vertical = pygame.image.load("brick_texture_vertical.png").convert()
        wallDim1 = 100
        wallDim2 = 21
        for i in range(0, self.num):
            dec = random.randrange(2, 20)
            x = random.randrange(60, 290)
            y = random.randrange(60, 290)
            if i % 2 == 0:
                tmp = wallDim1
                wallDim1 = wallDim2
                wallDim2 = tmp
            self.w_list.append( pygame.Rect( x, y, wallDim1, wallDim2 ) )
            self.w_list_of_pos.append((x, y))

    def draw_walls(self):
        for i in range(0, self.num):

            if self.w_list[i][2] == 100: # Note.
                #print("Horizontal wall!")
                screen.blit(self.image_horizontal, self.w_list[i])
            else:
                #print("Vertical wall!")
                screen.blit(self.image_vertical, self.w_list[i])
            #pygame.draw.rect(screen, Blue, self.w_list[i])

### This function will detect if either the player or monster hits a wall ###
    def wall_collision(self, sq1, sq2, keys):
        for wall in self.w_list:
            if sq1.rect.colliderect(wall):
                if keys[pygame.K_UP]:#sq1.direction == "up":
                    sq1.rect.top += sq1.speed

                if keys[pygame.K_DOWN]:# sq1.direction == "down":
                    sq1.rect.top -= sq1.speed

                if keys[pygame.K_LEFT]:# sq1.direction == "left":
                    sq1.rect.left += sq1.speed

                if keys[pygame.K_RIGHT]:# sq1.direction == "right":
                    sq1.rect.left -= sq1.speed


            if sq2.rect.colliderect(wall):
                if sq2.direction == "up":
                    sq2.rect.top += sq2.speed

                if sq2.direction == "down":
                    sq2.rect.top -= sq2.speed

                if sq2.direction == "left":
                    sq2.rect.left += sq2.speed

                if sq2.direction == "right":
                    sq2.rect.left -= sq2.speed
########################### END ###############################
