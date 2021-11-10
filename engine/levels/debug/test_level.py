from engine.levels.level import Level
from engine.player.obj_player import Player
from engine.objects.object import Object
from engine.objects.test_objects.test_object import Test_Object
from engine.objects.object_manager import Object_Manager
from engine.widgets.widget_components.button.wgc_button import Button

class DemoLevel(Level):
    def __init__(self, game):
        super().__init__(game)
        self.player = self.add_object(object={"Class": Player, "Name": "Player", "Rect": (100, 100, 80, 80),"Surf": 2})

    def load(self):
        pass

