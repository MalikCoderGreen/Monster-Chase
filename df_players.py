import random
import pygame
import pygame as pg


############# Colors for agents #############
Green = (0, 255, 0)
Red = (255, 0, 0)
dim = 20
screen_w = 400
screen_h = 400
screen = pygame.display.set_mode((screen_w, screen_h))
#############      END         ###############


#########   Class for monster  ###############
class DF_Monster():
    def __init__(self, speed, x, y):
        self.speed = speed
        self.x = x
        self.y = y
        self.rect = pygame.Rect( self.x, self.y, dim, dim )




    # Draw the monster to the screen.
    def draw(self, screen, color):
        pygame.draw.rect( screen, Green, self.rect )

    def move(self, px, py, speed=5): # chase movement
        # Movement along x direction
        if self.x > px:
            self.x -= speed
        elif self.x < px:
            self.x += speed
        # Movement along y direction
        if self.y < py:
            self.y += speed
        elif self.y > py:
            self.y -= speed



###############      END      ##############

# Class for user who will control this agent.
class User():
    def __init__(self, speed, x, y):
        self.speed = speed
        self.x = x
        self.y = y
        self.rect = pygame.Rect( self.x, self.y, dim, dim )

    def draw(self, screen, color):
        pygame.draw.rect( screen, color, self.rect )

    def updatePos(self, x, y):
        self.rect = self.rect.move(x, y)
        self.draw(screen, Red)

    def getPos(self):
        return [ self.x, self.y ]
