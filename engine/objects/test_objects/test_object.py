from engine.objects.object import Object
from engine.actions.actions.act_test import Test_Action


class Test_Object(Object):
    def ovr_init(self):
        #print("Test Object Spawned")
        self.sprite_path = r'.\assets\img\debug\joe.png'

    def ovr_on_overlap(self):
        test_action = Test_Action(self.game)
        test_action.play(objects=[self])

