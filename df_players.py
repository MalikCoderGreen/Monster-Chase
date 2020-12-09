import random
import pygame
import math


############# Colors for agents ##############
Green = (0, 255, 0)
Red = (255, 0, 0)
m_dim = 30
p_dim = 20
screen_w = 500
screen_h = 500
screen = pygame.display.set_mode((screen_w, screen_h))
#############      END         ###############


#########   Class for monster  ###############
class DF_Monster():
    def __init__(self, x, y):
        self.speed = 1
        self.direction = ""
        self.x = x
        self.y = y
        self.image = pygame.image.load("monster.png").convert()
        self.rect = pygame.Rect( self.x, self.y, m_dim, m_dim )
        self.scaledMonster = pygame.transform.scale(self.image, (int(m_dim), int(m_dim)))



    # Draw the monster to the screen.
    def draw(self):
        screen.blit(self.scaledMonster, self.rect)
        #pygame.draw.rect( screen, Green, self.rect )



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
        self.direction = "wait"
        self.x = x
        self.y = y
        self.image = pygame.image.load("dragon.png").convert()
        self.rect = pygame.Rect( self.x, self.y, p_dim, p_dim )
        #self.image.rect = self.rect
        self.scaledPlayer = pygame.transform.scale(self.image, (int(p_dim * 1.3), int(p_dim * 1.3)))

    def draw(self):
        #pygame.draw.rect( screen, color, self.rect )
        screen.blit(self.scaledPlayer, self.rect)


    def getPos(self):
        return ( self.rect.left, self.rect.top )

    def updateMove(self, keys):
        if keys[pygame.K_UP]:
            self.direction = "up"
            self.rect.top -= self.speed
        elif keys[pygame.K_DOWN]:
            self.direction = "down"
            self.rect.top += self.speed
        elif keys[pygame.K_LEFT]:
            self.direction = "left"
            self.rect.left -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.direction = "right"
            self.rect.left += self.speed
        else:
            self.direction = "wait"
