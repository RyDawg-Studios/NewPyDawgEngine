from engine.levels.level import Level
from engine.player.obj_player import Player
from engine.objects.object import Object
from engine.objects.test_objects.test_object import Test_Object
from engine.objects.object_manager import Object_Manager

class DemoLevel(Level):
    def load(self):

        self.add_object([Test_Object, "test", r'\img\debug\joe.png', (10, 10, 60, 60), 0])
        self.player = self.add_object([Player, "Player", r'\img\icon\thedawg.jpg', (100, 100, 80, 80), 2])

