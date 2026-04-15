import pygame
from sys import exit
from ship import ship
from background import back_ground
from opponent import opponent
from opponent2 import opponent2
from fire_bullet import bullet
from start_end_toggle import start_end

class star_war:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.screen = pygame.display.set_mode((800,400))
        self.image=ship(self.screen)
        self.image3=opponent(self.screen,self.image)
        self.image2=back_ground(self.screen)
        self.image4 = opponent2(self.screen,self.image)
        self.image5=bullet(self.screen,self.image,self.image3,self.image4)
        self.font=pygame.font.Font(None,100)
        # New Scoring System Fonts
        self.font = pygame.font.Font(None, 100)
        self.score_font = pygame.font.Font(None, 50)
        self.score = 0
        self.game_active=True
        self.start=start_end(self.screen)

    def game_text(self):
        text_surface= self.font.render("star war",False,"red")
        return text_surface
    
    def show_score(self):
        score_surface = self.score_font.render(f"Score: {self.score}", False, "green")
        self.screen.blit(score_surface, (20, 20))
   
    def caption(self):
        pygame.display.set_caption("star war")

    def background_colour(self):
        self.screen.fill((135,206,250))

    def reset_game(self):
        self.image.ship_rect.x = 375
        self.image.ship_rect.y = 350

        self.image3.attecker_rect.x = 320
        self.image3.attecker_rect.y = 0
        self.image3.remove1 = True
    
        self.image4.attecker2_rect.x = 320
        self.image4.attecker2_rect.y = 0
        self.image4.remove2 = True
        self.score = 0

        self.game_active = True

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif(event.type == pygame.KEYDOWN):
                    self.image.move3(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.start.s2toggle_rect.collidepoint(event.pos):
                            self.reset_game()
            if self.game_active==True:
                    
                self.image.mouse_move()
                self.background_colour()
                self.image2.place_background()
                self.screen.blit(self.game_text(),(250,50))
                self.image.place_ship()

                self.image5.move4()
                self.image5.place_bullat()
                self.image3.move2()
                self.image3.place_attecker()

                self.image4.move()
                self.image4.place_attecker2()
                self.show_score()
                if self.image3.collide():
                    self.game_active=False

                    
                if self.image4.collide2():
                    self.game_active=False
                    
                if self.image5.collide3():
                    self.score += 1
                    
            elif self.game_active==False:
                self.start.place_start_end()
                final_score_surf = self.score_font.render(f"Final Score: {self.score}", False, "yellow")
                self.screen.blit(final_score_surf, (280, 340))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.start.s2toggle_rect.collidepoint(event.pos):
                            self.game_active = True
            
            pygame.display.update()
            self.clock.tick(90)

if __name__ == '__main__':
    ai = star_war()
    ai.caption()
    ai.run_game()
    
    