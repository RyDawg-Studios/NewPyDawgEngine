from engine.levels.blueprints.blueprint import Blueprint

class Level():
    def __init__(self, game):
        print("Level Initialized")
        self.components = []
        self.game = game
        self.rapid = Blueprint(self, r"C:\Users\Administrator\Documents\GitHub\NewPyDawgEngine\engine\levels\blueprints\debug\bp_test.json")  #Rapid is a levels empty default blueprint, that is updated during gameplay


    def init(self):
        self.load()

    def load(self):
        pass

    def unload(self):
        self.components.clear()

    def update(self):
        for obj in self.components:
            obj.update()

    def add_object(self, object):
        new_obj = self.game.object_manager.spawn_object(object)
        self.components.append(new_obj)
        return new_obj

    def remove_object(self, object):
        self.components.remove(object)
        self.game.object_manager.remove_object(object)


