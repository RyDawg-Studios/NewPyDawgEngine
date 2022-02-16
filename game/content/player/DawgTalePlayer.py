from turtle import pos
from engine.actor.actor import Actor
from engine.gravity.gravity_component import GravityComponent
from engine.player.player_controller import PlayerController
from engine.sprite.sprite_component import SpriteComponent
from game.content.objects.coin.coin import Coin
from game.content.objects.projectile import Projectile


class DawgTalePlayer(Actor):
    def __init__(self, man, pde, scale=[16, 16], position=[600, 400]):
        self.scale = scale
        self.position=position
        self.maxHealth = 1
        self.health = self.maxHealth
        self.dead = False
        self.ticks = 0
        self.deadticks = 0
    
        super().__init__(man, pde)

        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'game\assets\heart.png', layer=1)
        self.components["PlayerController"] = PlayerController(owner=self)
        self.components["Gravity"] = GravityComponent(owner=self)

    def overlap(self, obj):
        if obj.__class__ == Projectile:
            if not self.dead:
                obj.deconstruct()
            self.health -= 1
            if self.health <=0:
                self.dead = True
        elif obj.__class__ == Coin:
            obj.deconstruct()
            self.man.add_object(Coin(man=self.man, pde=self.pde))

    def update(self):
        super().update()
        self.ticks += 1
        if self.dead:
            self.canMove = False
            self.deadticks += 1
            self.components["Sprite"].deconstruct()
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'game\assets\brokenheart.png', layer=1)
            if self.deadticks >= 100:
                self.pde.level_manager.removelevel('Main')
                self.pde.game.loadbattlelevel()



    def shoot(self):
        pass