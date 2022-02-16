import random
from engine.actor.actor import Actor
from game.content.objects.projectile import Projectile


class ProjectileSpawner(Actor):
    def __init__(self, man, pde, position):
        self.position = position
        super().__init__(man, pde)

        self.ticks = 0

        self.rot=0

        self.rotrate = random.randint(1,259)
        self.rotoffset = random.randint(1,12)
        self.projspeed = random.randint(3,12)
        self.projlifetime = 700
        self.ticktime = 999999



    def update(self):
        self.ticks += 1
        self.rot += self.rotrate

        if self.ticks <= self.ticktime:
            self.man.add_object(Projectile(man=self.man, pde=self.pde, position=[self.position[0], self.position[1]], rotation=self.rot, speed=[self.projspeed,self.projspeed], lifetime=self.projlifetime)) 
            if self.rot > 360:
                self.rot = self.rot-360 + self.rotoffset

