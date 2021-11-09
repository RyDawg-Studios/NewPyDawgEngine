from engine.levels.level import Level
from engine.widgets.widget_components.button.wgc_button import Button
import json

class Widget(Level):
    def __init__(self, game, path):
        super().__init__(self)
        print("Widget Initialized")
        self.components = []
        self.game = game
        self.path = path
        self.data = None
        self.init()


    def init(self):
        self.load()

    def load(self):
        raw = open(self.path, "r")
        self.data = json.load(raw)
        for wgc in self.data["Widget"]:
            #rawclass = eval(self.data["Widget"][wgc]["Class"],{"game": "self.game", "args": ["Nuts"]})
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






















