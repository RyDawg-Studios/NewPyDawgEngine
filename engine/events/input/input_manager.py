import pygame


class InputManager():
    def __init__(self, game):
        print("Input Manager Initialized")
        self.game = game
        self.key_inputs = []
        self.mouse_inputs = ()

    def update(self, event):

        self.mouse_inputs = pygame.mouse.get_pressed(5)

        if event.type == pygame.KEYDOWN:
            self.key_inputs.append(event.key)

        if event.type == pygame.KEYUP:
            self.key_inputs.remove(event.key)





        self.manage_inputs()

    def manage_inputs(self):
        if pygame.K_ESCAPE in self.key_inputs:
            self.game.exitgame()
