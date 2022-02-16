import pygame
import math
import random

screen = pygame.display.set_mode([400, 400])


class Bullet():
    def __init__(self, pos=[200,200], rot=[0,0], size=[0,0], spd=[1,1]) -> None:
        self.rot = rot
        self.pos = pos
        self.size = size
        self.spd = spd
        self.vel=[0,0]
        self.rect = pygame.rect.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.image = pygame.image.load(r'game/assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.image = pygame.transform.rotate(self.image, self.rot)
        self.ticks = 0


    def update(self):
        global bullets
        self.travel()
        screen.blit(self.image, (self.pos[0], self.pos[1]))
        if self.ticks >= 1000:
            bullets.remove(self)
            del self

    def updatevelocity(self):
        self.vel[0] = math.cos(math.radians(self.rot)) * self.spd[0]
        self.vel[1] = math.sin(math.radians(self.rot)) * self.spd[1] *-1

        return self.vel

    def travel(self):
        vel = self.updatevelocity()
        self.pos[0] += vel[0]
        self.pos[1] += vel[1]
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]


clock = pygame.time.Clock()
bullets = []
ticks = 0

while True:
    screen.fill((0,0,0))
    ticks += 1
    if ticks == 2:
        bullets.append(Bullet(rot=random.randint(0, 360), size=[16, 16], pos=[190,190]))
        ticks = 0

    for blt in bullets:
        blt.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    clock.tick(60)

    

    pygame.display.update()


