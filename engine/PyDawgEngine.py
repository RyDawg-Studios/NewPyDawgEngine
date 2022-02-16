import pygame
from engine.display.display_manager import DisplayManager
from engine.event.event_manager import EventManager
from engine.input.input_manager import InputManager
from engine.level.level_manager import LevelManager
from engine.mouse.mouse_manager import MouseManager
from engine.game.game import Game


class PyDawgEngine:

    def __init__(self) -> None:
        self.display_manager = DisplayManager(pde=self)
        self.display_manager.active = True

        self.event_manager = EventManager(pde=self)
        self.event_manager.active = True

        self.mouse_manager = MouseManager(pde=self)
        self.mouse_manager.active = True

        self.level_manager = LevelManager(pde=self)
        self.level_manager.active = True

        self.input_manager = InputManager(pde=self)
        self.input_manager.active = True

        self.clock = pygame.time.Clock()
        self.dt = 0
        self.targetFPS = 60
        self.fps = 0

        self.game = Game(pde=self)

        self.startengine()

    def startengine(self):
        for man in [self.display_manager, self.event_manager, self.mouse_manager, self.level_manager, self.input_manager]:
            if man.active == False:
                raise Exception(str(man) + " Was not active on engine start. Did you properly initialize it?")
            else: man.activate()

        while True:
            self.update()





    def update(self):
        self.event_manager.update()
        self.mouse_manager.update()
        self.level_manager.update()
        self.game.update()
        self.display_manager.update()

        self.dt = self.clock.tick(60) * 0.001 * self.targetFPS
        self.fps = round(self.clock.get_fps())

        #pygame.display.set_caption(str(self.fps))


        
