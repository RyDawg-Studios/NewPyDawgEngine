import pygame
from engine.object.object import Object
from engine.debug.debugLevel import TestLevel

class Game:
    def __init__(self, pde):
        self.pde = pde
        self.pde.level_manager.addlevel(level=TestLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)

    def update(self):
        pygame.display.set_caption(str(self.pde.level_manager.levels["Main"].defaultObjectManager.objects.keys()))

