class Object:
    def __init__(self, man, pde, components={}, *args) -> None:
        self.manager = man
        self.pde = pde
        self.name = str(self.__class__)
        self.components = components
        
        for comp in self.components:
            comp = self.add_component(name=comp, component=components[comp])
            


    def add_component(self, component, name):
        component['args']['owner'] = self
        tempcomp = component["class"](kwargs = component['args'])
        self.components[name] = tempcomp
        return tempcomp
        

    def remove_component(self, component):
        self.components.pop(component)

    def update(self):
        for component in self.components:
            self.components[component].update()