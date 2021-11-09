import json
from engine.objects.test_objects.test_object import Test_Object



class Blueprint():
    def __init__(self, level, association):
        self.level = level
        self.objects = []
        if association != None:
            self.data = self.load(association=association)
        else:
            pass


        self.spawn()


    def spawn(self):
        """Spawn entire blueprint"""
        for obj in self.data["Blueprint"]:
            temp = eval(self.data["Blueprint"][obj]["Class"])
            self.level.add_object(temp, "old")


    def despawn(self):
        """Unload entire blueprint"""
        pass

    def remove(self):
        """Remove individual object from blueprint"""
        pass

    def load(self, association):
        raw = open(association, "r")
        data = json.load(raw)

        return data