import pygame
class ship():
    def __init__(self,screen):
        self.ship=pygame.image.load('image4.png').convert_alpha()
        self.ship = pygame.transform.scale(self.ship, (50, 50))
        self.ship_rect= self.ship.get_rect(midbottom= (80,80))
        self.ship_rect.x = 375
        self.ship_rect.y = 350
        self.screen=screen

        
    def move3(self,event):
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT   :
            #here we move the ship to the right 2px
            self.ship_rect.x += 10
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT   :
            #here we move the ship to the LEFT 2px
            self.ship_rect.x -= 10
        elif event.key == pygame.K_w or event.key == pygame.K_UP   :
            self.ship_rect.y -= 10
        elif event.key == pygame.K_x or event.key == pygame.K_DOWN   :
            self.ship_rect.y += 10
    def mouse_move(self):
        buttons = pygame.mouse.get_pressed()

        if buttons[0]:
              if self.ship_rect.collidepoint(pygame.mouse.get_pos()):
                self.ship_rect.center = pygame.mouse.get_pos()
        
        
  
    def place_ship(self):
        self.screen.blit(self.ship,(self.ship_rect))
