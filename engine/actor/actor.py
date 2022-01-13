import pygame
from engine.object.object import Object
from engine.sprite.sprite_component import SpriteComponent

class Actor(Object):
    position = [10, 10]
    scale = [30, 30]
    rect = [position[0], position[1], scale[0], scale[1]]

    def __init__(self, man, pde, components={}) -> None:
        super().__init__(man, pde, components=components)
        

    def update(self):
        super().update()
        pass