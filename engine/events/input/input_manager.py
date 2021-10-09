import pygame


class InputManager():
    def __init__(self, game):
        print("Input Manager Initialized")
        self.game = game
        self.inputs = []

    def update(self, event):

        if event.type == pygame.KEYDOWN:
            self.inputs.append(event.key)

        if event.type == pygame.KEYUP:
            self.inputs.remove(event.key)

        self.manage_inputs()

    def manage_inputs(self):
        if pygame.K_ESCAPE in self.inputs:
            self.game.exitgame()
