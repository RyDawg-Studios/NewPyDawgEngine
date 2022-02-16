import pygame
from pygame.sprite import AbstractGroup
from engine.component.component import Component
import math

class Sprite(pygame.sprite.Sprite):
    def __init__(self, parent, sprite, layer: AbstractGroup) -> None:
        super().__init__()

        self.parent = parent
        self.layer= layer


        self.image = pygame.image.load(sprite)
        self.image = pygame.transform.scale(self.image, (self.parent.scale[0],self.parent.scale[1]))
        self.image = pygame.transform.rotate(self.image, self.parent.rotation)

        if layer in parent.pde.display_manager.surfs:
            parent.pde.display_manager.surfs[layer].append(self)
        else:
            parent.pde.display_manager.createsurf(id=layer)
            parent.pde.display_manager.surfs[layer].append(self)

    def deconstruct(self):
        try:
            self.parent.pde.display_manager.surfs[self.layer].remove(self)
        except:
            pass
        del self




class SpriteComponent(Component):
    def __init__(self, owner, sprite, layer=0, **kwargs) -> None:
        super().__init__(owner, **kwargs)
        
        self.sprite = Sprite(owner, sprite, layer)

    def deconstruct(self):
        self.sprite.deconstruct()
        super().deconstruct()