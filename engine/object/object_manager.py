import pygame

class ObjectManager:
    def __init__(self, pde) -> None:
        self.pde = pde
    
    objects = {}

    def add_object(self, obj):
        self.objects[obj.name] = obj

    def remove_object(self, obj):
        if obj in self.objects.keys():
            self.objects.pop(obj)


    def update(self):
        for obj in self.objects:
            self.objects[obj].update()



