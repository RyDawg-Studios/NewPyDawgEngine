import pygame


class Settings_Manager:
    def __init__(self, game):
        self.game = game

        self.up_key = pygame.K_UP
        self.down_key = pygame.K_DOWN
        self.left_key = pygame.K_LEFT
        self.right_key = pygame.K_RIGHT
        self.rotate_l_key = pygame.K_z
        self.rotate_r_key = pygame.K_x
        self.debug_key = pygame.K_f

    def update(self):
        pass


settings = {"Dimensions": (500, 400)}
