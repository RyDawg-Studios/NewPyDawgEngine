class LevelManager:
    def __init__(self, pde) -> None:
        self.pde = pde
        self.levels={}

    def addlevel(self, level, name, active):
        level.active = active
        self.levels[name] = level

    def removelevel(self, level):
        self.levels.pop(level)

    def update(self):
        for level in self.levels:
            if self.levels[level].active:
                self.levels[level].update()