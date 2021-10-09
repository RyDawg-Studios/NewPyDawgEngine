from engine.levels.level import Level

class Widget(Level):
    def __init__(self, game):
        super().__init__(self)
        pass
        print("Widget Initialized")
        self.components = []
        self.game = game


    def init(self):
        self.load()

    def load(self):
        pass

    def unload(self):
        self.components = []

    def update(self):
        for component in self.components:
            component.update()

    def add_object(self, object):
        new_obj = self.game.object_manager.spawn_object(object)
        self.components.append(new_obj)
        return new_obj






















