import pygame
from engine.object.object import Object
from engine.actor.actor import Actor
from engine.component.component import Component

class TestObject(Object):
    def __init__(self, man, pde, components={}, *args) -> None:
        super().__init__(man, pde, components=components, *args)


class TestActor(Actor):
    rect = pygame.Rect([10, 10, 30, 30])
    def __init__(self, man, pde, components={}) -> None:
        super().__init__(man, pde, components=components)



        


