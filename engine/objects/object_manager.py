import pygame
from engine.objects.object import Object

class Object_Manager():
    def __init__(self, game):
        self.game = game

        self.all_objects = []


    def update(self):
        for object in self.all_objects:
            object.update()


    def spawn_object(self, object, args):  #[ObjClass, Name, Rect, Surface_Index]
        new_object = object["Class"](self.game, struct=object, args=args)
        self.all_objects.append(new_object)
        return new_object

    def remove_object(self, obj):
        obj.destroy()
        self.all_objects.remove(obj)


