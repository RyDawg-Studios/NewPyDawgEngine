from engine.objects.object import Object
from engine.game_events.events.ev_test import Test_Event


class Test_Object(Object):
    def ovr_init(self):
        self.test_event = Test_Event(self.game)
        print("Test Object Spawned")

    def ovr_on_overlap(self):
        self.test_event.play(objects=[self])

