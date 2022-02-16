import pygame
import json


class DisplayManager:
    def __init__(self, pde) -> None:
        self.active = False
        self.pde = pde
        self.surfs = {}

        self.screen = pygame.display.set_mode((640, 480))
        self.bg = False

        self.bgimg = ''

        file = open(r"engine\cfg\engineconfig.json")
        self.cfg = json.load(file)


    def update(self):
        if self.bg == False:
            self.screen.fill((0,0,0))
        for surf in list(self.surfs.values()):
            for spr in surf:
                self.screen.blit(spr.image, (spr.parent.position[0], spr.parent.position[1]))
                

        pygame.display.update()



    def configurewindow(self):

        cap = self.cfg["config"]["caption"]
        pygame.display.set_caption(cap)

        self.createsurf(id=0)

    def createsurf(self, id=None):
        if id != None:
            self.surfs[id] = []

    def changebackground(self, image):
        self.bg = pygame.image.load(image)
        self.bg = pygame.transform.scale(image, [100, 100])
        self.surfs[0].blit(self.bg, (10,10,10,10))

    def activate(self):
        self.configurewindow()




