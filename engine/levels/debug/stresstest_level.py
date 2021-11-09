from engine.levels.level import Level
from engine.objects.test_objects.test_object import Test_Object
from engine.player.obj_plghost import Player
import random
import pygame



class StressLevel(Level):
    def __init__(self, game):
        super().__init__(game)

        self.player = self.add_object([Player, "ghost", Player.spritepath, (100, 100, 80, 80), 2])
        for i in range(0, 100):
            self.object = self.add_object([Test_Object, "TheGuy", r'\img\icon\thedawg.jpg', (random.randint(0, 490),random.randint(0, 390), 80, 80), 2])

    def load(self):
        pass

    def update(self):
        pygame.display.set_caption("FPS: " + str(self.game.clock.get_fps()))
