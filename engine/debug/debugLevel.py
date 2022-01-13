from engine.level.level import Level
from engine.debug.debugObject import TestActor, TestObject
from engine.sprite.sprite_component import SpriteComponent
from engine.player.player_controller import PlayerController

class TestLevel(Level):
    def __init__(self, man, pde) -> None:
        super().__init__(man, pde)
        #self.defaultObjectManager.add_object(obj=TestObject(man=self.defaultObjectManager, pde=pde))
        self.defaultObjectManager.add_object(obj=TestActor(man=self.defaultObjectManager, pde=pde, components={"SpriteComponent": {'class': SpriteComponent, 'args': {'sprite': 'assets\debug\sprites\debug.png'}}, 
                                                                                                                "PlayerController": {'class': PlayerController, 'args':{}}}))