import pygame
from engine.objects.object import Object

class Object_Manager():
    def __init__(self, game):
        self.game = game

        self.all_objects = []


    def update(self):
        for object in self.all_objects:
            object.update()


    def spawn_object(self, args): # [ObjClass, Name, Path, Rect, Surface_Index]
        new_object = args[0](self.game, args)
        self.all_objects.append(new_object)
        return new_object

