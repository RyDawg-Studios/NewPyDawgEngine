from engine.objects.object import Object
from engine.actions.actions.act_test import Test_Action


class Test_Object(Object):
    def ovr_init(self):
        self.test_event = Test_Action(self.game)
        #print("Test Object Spawned")
        self.spritepath = r'\img\debug\joe.png'

    def ovr_on_overlap(self):
        self.test_event.play(objects=[self])

