import pygame
import random 
class opponent2():
    
    def __init__(self,screen,ship):
        self.attecker2 = pygame.image.load('picture5.png').convert_alpha()
        self.attecker2 = pygame.transform.scale(self.attecker2, (50, 50))
        self.attecker2_rect =self.attecker2.get_rect(midbottom= (80,80))
        self.attecker2_rect.x = 320
        self.attecker2_rect.y = 0
        self.screen=screen
        self.ship=ship
        self.remove2 = True
        self.game_active=True
    def move(self):
        self.attecker2_rect.y += 2
        if self.attecker2_rect.y > 400:
            self.attecker2_rect.y = 0
            self.attecker2_rect.x = random.randint(0,780)
    def respawn(self):
        self.attecker2_rect.y = 0
        self.attecker2_rect.x = random.randint(0,780)
        

    def place_attecker2(self):
        if self.remove2 == True:
           self.screen.blit(self.attecker2,(self.attecker2_rect))
    def collide2(self):
        if self.attecker2_rect.colliderect(self.ship.ship_rect):
            return True
            
