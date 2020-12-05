import random
import pygame
import math


############# Colors for agents ##############
Green = (0, 255, 0)
Red = (255, 0, 0)
dim = 20
screen_w = 400
screen_h = 400
screen = pygame.display.set_mode((screen_w, screen_h))
#############      END         ###############


#########   Class for monster  ###############
class DF_Monster():
    def __init__(self, x, y):
        self.speed = 1
        self.direction = ""
        self.x = x
        self.y = y
        self.rect = pygame.Rect( self.x, self.y, dim, dim )



    # Draw the monster to the screen.
    def draw(self, screen, color):
        pygame.draw.rect( screen, Green, self.rect )



    def findPlayer(self, px, py): # chase movement
        # Movement along x direction
        if self.x > px:
            self.direction = "left"
            self.rect.move_ip( -self.speed, 0 )
        if self.x < px:
            self.direction = "right"
            self.rect.move_ip( self.speed, 0 )
        # Movement along y direction
        if self.y < py:
            self.direction = "down"
            self.rect.move_ip( 0, self.speed )
        if self.y > py:
            self.direction = "up"
            self.rect.move_ip( 0, -self.speed )

    def getPos(self):
        return ( self.rect.left, self.rect.top )




###############      END      ##############

# Class for user who will control this agent.
class User():
    def __init__(self, x, y):
        self.speed = 1
        self.direction = ""
        self.x = x
        self.y = y
        self.rect = pygame.Rect( self.x, self.y, dim, dim )

    def draw(self, screen, color):
        pygame.draw.rect( screen, color, self.rect )


    def getPos(self):
        return ( self.rect.left, self.rect.top )

    def updateMove(self, keys):
        if keys[pygame.K_UP]:
            self.direction = "up"
            self.rect.top -= self.speed
        if keys[pygame.K_DOWN]:
            self.direction = "down"
            self.rect.top += self.speed
        if keys[pygame.K_LEFT]:
            self.direction = "left"
            self.rect.left -= self.speed
        if keys[pygame.K_RIGHT]:
            self.direction = "right"
            self.rect.right += self.speed
