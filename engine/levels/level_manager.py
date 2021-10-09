class Level_Manager():
    def __init__(self, game):
        print("Level Manager Initialized")
        self.current_level = None
        self.game = game

    def init(self, level):
        self.current_level = level
        self.current_level.load()

    def load_level(self, level):
        if self.current_level != None:
            level.load(self.game)

        else:
            self.current_level.unload()
            self.current_level = level

    def update(self):
        self.current_level.update()


