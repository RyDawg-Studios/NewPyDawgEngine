import pygame

class DisplayManager():
    def __init__(self, game):
        print("Display Manager Initialized")
        self.game = game
        self.bg_surf_bottom = pygame.display.set_mode((500, 400))
        self.bg_surf_top = pygame.display.set_mode((500, 400))
        self.bottom_surf = pygame.display.set_mode((500, 400))
        self.mid_surf = pygame.display.set_mode((500, 400))
        self.top_surf = pygame.display.set_mode((500, 400))
        self.wg_surf_bottom = pygame.display.set_mode((500, 400))
        self.wg_surf_top = pygame.display.set_mode((500, 400))


        self.surfs = [self.bottom_surf, self.mid_surf, self.top_surf, self.bg_surf_bottom, self.bg_surf_top, self.wg_surf_bottom, self.wg_surf_top]
        pygame.display.set_caption("PyDawgEngine")


    def update(self):
        pygame.display.update()
        for surface in self.surfs:
            surface.fill((0, 0, 0))



