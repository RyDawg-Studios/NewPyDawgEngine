from engine.actions.action import Action
from engine.levels.debug.test_level2 import DemoLevel2

class Test_Action(Action):
    def play(self, objects):
        self.game.level_manager.load_level(DemoLevel2)


