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
        self.event_manager = EventManager(pde=self)
        self.mouse_manager = MouseManager(pde=self)
        self.level_manager = LevelManager(pde=self)
        self.input_manager = InputManager(pde=self)
        self.clock = pygame.time.Clock()

        self.game = Game(pde=self)

        self.startengine()


    def update(self):
        self.event_manager.update()
        self.mouse_manager.update()
        self.level_manager.update()
        self.game.update()
        self.display_manager.update()


        self.clock.tick(60)


        


    def startengine(self):
        while True:
            self.update()


