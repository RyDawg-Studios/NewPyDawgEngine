import pygame
from pygame import display


class MouseManager():
    def __init__(self, pde):
        self.pde = pde
        self.pos = [0, 0]

    def update(self):
        self.pos = pygame.mouse.get_pos()

        #self.mouse_rect = (self.pos[0], self.pos[1], 10, 10)
        #pygame.draw.rect(self.pde.display_manager.display, (255, 255,255), self.mouse_rect)