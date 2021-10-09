import pygame


class Mouse_Manager():
    def __init__(self, game):
        self.game = game
        print("Mouse Manager Initialized")
        self.location = (0, 0)

    def update(self):
        self.location = pygame.mouse.get_pos()
        #self.mouse_rect = (self.location[0], self.location[1], 10, 10)
        #pygame.draw.rect(self.game.display_manager.surfs[6], (255, 255,255), self.mouse_rect)




        #PLEASE FINISH UI STUFF TODAY - RyDawgE 10/9/21

