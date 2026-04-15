import pygame
from ship import ship



class bullet():
    def __init__(self,screen,ship,opponent,opponent2):
        self.bullat=pygame.image.load('bullat_image.png').convert_alpha()
        self.bullat = pygame.transform.scale(self.bullat, (30, 30))
        self.bullat = pygame.transform.rotate(self.bullat, 90)
        self.bullat_rect= self.bullat.get_rect(midbottom= (80,80))

        self.screen=screen
        self.ship=ship
        self.bullat_rect.x = self.ship.ship_rect.x+50
        self.bullat_rect.y = self.ship.ship_rect.y
        self.oppnent=opponent
        self.oppnent2=opponent2
       

    def move4(self):
        self.bullat_rect.y -= 8
        if self.bullat_rect.y < 0:
            self.bullat_rect.y = self.ship.ship_rect.y-20
            self.bullat_rect.x = self.ship.ship_rect.x+10

    def place_bullat(self):
          self.screen.blit(self.bullat,(self.bullat_rect))
        
    def collide3(self):
        hit = False
        if self.bullat_rect.colliderect(self.oppnent.attecker_rect):
            self.oppnent.respawn()      
            self.bullat_rect.y = -10    
            hit = True
        elif self.bullat_rect.colliderect(self.oppnent2.attecker2_rect):
            self.oppnent2.respawn()     
            self.bullat_rect.y = -10    
            hit = True  
        return hit