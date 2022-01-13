import pygame
from engine.input.input_manager import InputManager

class EventManager:
    def __init__(self, pde) -> None:
        self.pde = pde

        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            self.pde.input_manager.update(event)
