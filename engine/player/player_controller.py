import pygame
from engine.component.component import Component

class PlayerController(Component):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.inpman = self.owner.pde.input_manager
        self.max_player_speed = 2
        
        
    def update(self):
        self.update_velocity()
        return super().update()



    def update_velocity(self):
        if pygame.K_d in self.owner.pde.input_manager.key_inputs:
            self.owner.rect.x += self.max_player_speed
        if pygame.K_a in self.owner.pde.input_manager.key_inputs:
            self.owner.rect.x -= self.max_player_speed
        if pygame.K_w in self.owner.pde.input_manager.key_inputs:
            self.owner.rect.y -= self.max_player_speed
        if pygame.K_s in self.owner.pde.input_manager.key_inputs:
            self.owner.rect.y += self.max_player_speed