from engine.levels.level import Level
from engine.player.obj_player import Player

class DemoLevel2(Level):
    def __init__(self, game):
        super().__init__(game)
        self.player = self.add_object([Player, "Player", r'\img\icon\thedawg.jpg', (100, 100, 80, 80), 2])
        self.test_object = self.add_object([Test_Object, "test", r'\img\debug\joe.png', (200, 10, 60, 60), 0])

    def load(self):
        pass

