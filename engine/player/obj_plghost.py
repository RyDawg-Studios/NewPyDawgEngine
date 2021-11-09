from engine.objects.object import Object
import pygame
class Player(Object):
    spritepath = 'none'
    checkForCollision = False

    def ovr_init(self):
        print("Ghost Player Spawned")
        self.spritepath = 'none'







