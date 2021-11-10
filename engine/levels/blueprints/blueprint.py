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
        for o in self.data["Blueprint"]:
            cls = eval(self.data["Blueprint"][o]["Class"])
            obj = {"Class": cls,
                   "Name": self.data["Blueprint"][o]["Name"],
                   "Rect": eval(self.data["Blueprint"][o]["Rect"]),
                   "Surf": self.data["Blueprint"][o]["Layer"]}
            self.level.add_object(object=obj)


    def despawn(self):
        """Unload entire blueprint"""
        for o in self.objects:
           self.level.remove_object(o)
    def remove(self, obj):
        """Remove individual object from blueprint"""
        self.level.remove_object(obj)

    def load(self, association):
        raw = open(association, "r")
        data = json.load(raw)

        return data