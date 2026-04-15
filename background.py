import pygame
class back_ground():
    def __init__(self,screen):
        self.background=pygame.image.load('image2.jpg').convert()
        self.background = pygame.transform.scale(self.background, (800, 400))
        self.screen=screen
    def place_background(self):
        self.screen.blit(self.background,(0,0))