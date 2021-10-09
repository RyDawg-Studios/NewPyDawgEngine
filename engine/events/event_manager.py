import pygame

class EventManager():
    def __init__(self, game):
        print("Event Manager Initialized")
        self.game = game

    def update(self, event):
        if event.type == pygame.QUIT:
            self.game.exitgame()

        if event.type == pygame.KEYDOWN or pygame.KEYUP:
            self.game.input_manager.update(event)

        return