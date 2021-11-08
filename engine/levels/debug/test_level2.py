from engine.levels.level import Level
from engine.player.obj_player import Player

class DemoLevel2(Level):
    def __init__(self, game):
        super().__init__(game)
        self.player = self.add_object([Player, "Player", r'\img\icon\thedawg.jpg', (100, 100, 80, 80), 2])

