import pygame
from pygame.sprite import AbstractGroup
from engine.component.component import Component

class Sprite(pygame.sprite.Sprite):
    def __init__(self, actor, sprite, layer, *groups: AbstractGroup) -> None:
        super().__init__(*groups)

        self.rect = actor.rect
        self.rect.center = (self.rect[2] / 2, self.rect[3] / 2)

        self.image = pygame.image.load(sprite)
        self.image = pygame.transform.scale(self.image, (self.rect.size[0],self.rect.size[1]))

        self.rect.x = actor.position[0]
        self.rect.y = actor.position[1]

        actor.pde.display_manager.groups[layer].add(self)





class SpriteComponent(Component):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.sprite = Sprite(self.kwargs['owner'], self.kwargs['sprite'], layer=0)
