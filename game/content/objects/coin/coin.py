from random import random
from engine.actor.actor import Actor
from engine.sprite.sprite_component import SpriteComponent
import random


class Coin(Actor):
    def __init__(self, man, pde, pos=[0,0]):
        self.position = [random.randint(0, 640), random.randint(0,480)]
        self.checkForOverlap = True
        self.checkForCollision = False
        super().__init__(man, pde)

        self.components["Sprite"] = SpriteComponent(owner=self, sprite='game/assets/coin.png', layer=2)