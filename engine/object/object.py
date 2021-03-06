from heapq import merge


class Object:
    def __init__(self, man, pde, components={}) -> None:
        self.man = man
        self.pde = pde
        self.components = {}

    def removecomponent(self, component):
        self.components.pop(component)

    def update(self):
        for component in self.components:
            self.components[component].update()

    def deconstruct(self):
        self.man.remove_object(self)
        for component in self.components.values():
            component.deconstruct()
        del self


