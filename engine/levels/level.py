class Level():
    def __init__(self, game):
        print("Level Initialized")
        self.objects = []
        self.game = game


    def init(self):
        self.load()

    def load(self):
        pass

    def unload(self):
        self.objects = []

    def update(self):
        for object in self.objects:
            object.update()

    def add_object(self, object):
        new_obj = self.game.object_manager.spawn_object(object)
        self.objects.append(new_obj)
        return new_obj


