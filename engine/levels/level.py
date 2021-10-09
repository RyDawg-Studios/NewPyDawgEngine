class Level():
    def __init__(self, game):
        print("Level Initialized")
        self.components = []
        self.game = game


    def init(self):
        self.load()

    def load(self):
        pass

    def unload(self):
        self.components = []

    def update(self):
        for object in self.components:
            object.update()

    def add_object(self, object):
        new_obj = self.game.object_manager.spawn_object(object)
        self.components.append(new_obj)
        return new_obj


