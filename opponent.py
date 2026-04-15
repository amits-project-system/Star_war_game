import pygame
import random 
class opponent():
    
    def __init__(self,screen,ship):
        self.attecker = pygame.image.load('image3.png').convert_alpha()
        self.attecker = pygame.transform.scale(self.attecker, (50, 50))
        self.attecker_rect =self.attecker.get_rect(midbottom= (80,80))
        self.attecker_rect.x = 320
        self.attecker_rect.y = 0
        self.screen=screen
        self.ship=ship
        self.remove1 = True
        
        self.game_active=True
    def move2(self):
        self.attecker_rect.y += 2
        if self.attecker_rect.y > 400:
            self.attecker_rect.y = 0
            self.attecker_rect.x = random.randint(0,780)
    def respawn(self):
        self.attecker_rect.y = 0
        self.attecker_rect.x = random.randint(0,780)
   
    def place_attecker(self):
        if self.remove1 == True:
           self.screen.blit(self.attecker,(self.attecker_rect))
    def collide(self):
        if self.attecker_rect.colliderect(self.ship.ship_rect):
          return True
    
