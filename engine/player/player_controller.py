from re import I
import pygame
from engine.component.component import Component
from engine.action.queues.queue import Queue

class PlayerController(Component):
    def __init__(self, owner, **kwargs) -> None:
        super().__init__(owner, **kwargs)
        self.inpman = self.owner.pde.input_manager
        self.max_player_speed = 2
        self.saved_pos = [0,0]
        self.test_queue = Queue()

        
    def update(self):
        if self not in self.owner.pde.game.player_controllers:
            self.owner.pde.game.player_controllers.append(self)
        self.update_velocity()
        self.update_debug()
        return super().update()

    def update_velocity(self):
        maxSpeed = self.owner.maxSpeed
        if pygame.K_RIGHT in self.owner.pde.input_manager.key_inputs:
            self.owner.speed[0] = maxSpeed[0]

        elif pygame.K_LEFT in self.owner.pde.input_manager.key_inputs:
            self.owner.speed[0] = -maxSpeed[0]
        else: self.owner.speed[0] = 0

        if pygame.K_UP in self.owner.pde.input_manager.key_inputs:
            self.owner.speed[1] = -maxSpeed[1]

        elif pygame.K_DOWN in self.owner.pde.input_manager.key_inputs:
            self.owner.speed[1] = maxSpeed[1]
        else: self.owner.speed[1] = 0

    def update_debug(self):
        pass

    def on_input(self, input):
        if input == pygame.K_f:
            self.saved_pos = [self.owner.rect.x, self.owner.rect.y]
            print("Position Logged @ " + str(self.saved_pos))
        if input == pygame.K_g:
            self.owner.rect.x, self.owner.rect.y = self.saved_pos
            print("Position Loaded @ " + str(self.saved_pos))
        if input == pygame.K_r:
            self.owner.pde.level_manager.removelevel("Main")
            self.owner.pde.game.loadstresslevel()

        if input == pygame.MOUSEBUTTONDOWN:
            print("Shalom")

    def deconstruct(self):
        try: 
            self.owner.pde.game.player_controllers.remove(self)
        except:
            pass
        return super().deconstruct()