from engine.object.object_manager import ObjectManager
class Level:
    def __init__(self, man, pde) -> None:
        self.pde = pde
        self.manager = man
        self.active = False
        self.background = ''
        self.defaultObjectManager = ObjectManager(pde=pde)

    def update(self):
        self.defaultObjectManager.update()
