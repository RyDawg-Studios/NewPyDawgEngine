from engine.actions.action import Action

class Destroy_Action(Action):
    def play(self, objects):
        for o in objects:
            if o != "Player":
                self.game.level_manager.current_level.rapid.remove(o)

