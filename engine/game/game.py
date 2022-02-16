from engine.debug.debugLevel import TestLevel
from engine.debug.stressTestLevel import StressLevel
from game.content.levels.battle import BattleLevel
from game.content.levels.game_over import GameOverLevel


class Game:
    def __init__(self, pde):
        self.pde = pde
        self.pde.level_manager.addlevel(level=BattleLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)
        self.player_controllers = []

    def update(self):
        pass

    def loadstresslevel(self):
        self.pde.level_manager.addlevel(level=StressLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)
    def loadbattlelevel(self):
        self.pde.level_manager.addlevel(level=BattleLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)
    def loadgameoverlevel(self, pos):
        self.pde.level_manager.addlevel(level=GameOverLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True, pos=pos)
