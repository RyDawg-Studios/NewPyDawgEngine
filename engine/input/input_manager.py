import pygame


class InputManager():
    def __init__(self, pde):
        self.active = False
        self.pde = pde
        self.key_inputs = []
        self.mouse_inputs = ()

    def update(self, event):
        self.manage_inputs(event)
        #pygame.display.set_caption(str(self.key_inputs))

    def manage_inputs(self, event):
        self.mouse_inputs = pygame.mouse.get_pressed(5)

        if event.type == pygame.KEYDOWN:
            self.key_inputs.append(event.key)
            for player in self.pde.game.player_controllers:
                player.on_input(event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for player in self.pde.game.player_controllers:
                player.on_input(event.type)

        if event.type == pygame.KEYUP:
            self.key_inputs.remove(event.key)

        if pygame.K_ESCAPE in self.key_inputs:
            pygame.quit()
            quit()

    def activate(self):
        pass
