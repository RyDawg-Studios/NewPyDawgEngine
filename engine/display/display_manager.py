import pygame
import json


class DisplayManager:
    def __init__(self, pde) -> None:
        self.pde = pde
        self.surfs = {}
        self.groups = {}

        file = open(r".\engine\cfg\engineconfig.json")
        self.cfg = json.load(file)

        self.configurewindow()


    def update(self):
        pygame.display.update()
        for group in sorted(self.groups.keys()):
            self.surfs[group].fill((0, 0, 0))
            self.groups[group].update()
            self.groups[group].draw(self.surfs[group])



    def configurewindow(self):

        cap = self.cfg["config"]["caption"]
        pygame.display.set_caption(cap)

        self.createsurf(id=0)

    def createsurf(self, id=None):
        dims = eval(self.cfg["config"]["dimensions"])
        self.surfs[id] = pygame.display.set_mode(dims)
        self.groups[id] = pygame.sprite.Group()




