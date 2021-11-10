from engine.levels.level import Level
from engine.widgets.widget_components.button.wgc_button import Button
from engine.widgets.widget_components.button.buttons.wgc_test_button import TestButton
import json

class Widget():
    def __init__(self, game, path):
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
            cls = eval(self.data["Widget"][wgc]["Class"])



            #obj = cls(self.game, {"Name": self.data["Widget"][wgc]["Name"],
            #                      "Rect": eval(self.data["Widget"][wgc]["Rect"]),
            #                      "Surf": self.data["Widget"][wgc]["Surf"],
            #                      "Class": eval(self.data["Widget"][wgc]["Class"])},
            #          Path= eval(self.data["Widget"][wgc]["Path"]))
            self.add_new_object(object={"Name": self.data["Widget"][wgc]["Name"],
                                  "Rect": eval(self.data["Widget"][wgc]["Rect"]),
                                  "Surf": self.data["Widget"][wgc]["Surf"],
                                  "Class": eval(self.data["Widget"][wgc]["Class"])},
                                Path=r'.\assets\img\debug\test_button.png')



    def unload(self):
        self.components = []

    def update(self):
        for component in self.components:
            component.update()

    def add_new_object(self, object, **kwargs):
        new_obj = self.game.object_manager.spawn_object(object=object, args=kwargs)
        self.components.append(new_obj)
        return new_obj

