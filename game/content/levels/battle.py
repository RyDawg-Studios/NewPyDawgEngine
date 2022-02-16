from turtle import position
from engine.level.level import Level
from game.content.objects.coin.coin import Coin
from game.content.objects.projectile import Projectile
from game.content.objects.projectile_spawner import ProjectileSpawner
from game.content.player.DawgTalePlayer import DawgTalePlayer
import random

class BattleLevel(Level):
    def __init__(self, man, pde) -> None:
        self.ticks = 0
        self.rot=0
        super().__init__(man, pde)
        #self.changebackground(r'assets\debug\sprites\xp.png')

        self.objectManager.add_object(DawgTalePlayer(man=self.objectManager, pde=pde, position=[310, 400]))
        self.objectManager.add_object(ProjectileSpawner(man=self.objectManager, pde=pde, position=[320,240]))
        self.objectManager.add_object(Coin(man=self.objectManager, pde=pde))


    def update(self):
        pass

        
        return super().update()
        