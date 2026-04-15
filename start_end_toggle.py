import pygame
class start_end():
    def __init__(self,screen):
        self.s1toggle=pygame.image.load('image4.png').convert_alpha()
        self.s1toggle = pygame.transform.scale(self.s1toggle , (150, 150))
        self.s1toggle_rect= self.s1toggle.get_rect(center= (400,100))
        self.s2toggle=pygame.image.load('start.png').convert_alpha()
        self.s2toggle = pygame.transform.scale(self.s2toggle,(100, 100))
        self.s2toggle_rect= self.s2toggle.get_rect(center= (400,280))
        self.font=pygame.font.Font(None,30)
        self.screen=screen
    def game_text(self):
        text_surface= self.font.render("tab, to start the game",False,"red")
        return text_surface
    def place_start_end(self):
        self.screen.fill('blue')
        self.screen.blit(self.game_text(),(300,180))
        self.screen.blit(self.s1toggle,(self.s1toggle_rect))
        self.screen.blit(self.s2toggle,(self.s2toggle_rect))