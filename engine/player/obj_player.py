from engine.objects.object import Object
import pygame
from engine.game_events.events.ev_test import Test_Event
class Player(Object):
    def ovr_init(self):
        print("Player Spawned")
        self.max_player_speed = 3
        self.checkForCollision = True
        self.test_event = Test_Event(self.game)

    def ovr_update(self):
        self.update_velocity()

    def update_velocity(self):
        if self.game.settings.right_key in self.game.input_manager.inputs:
            self.rect.x += self.max_player_speed
        if self.game.settings.left_key in self.game.input_manager.inputs:
            self.rect.x -= self.max_player_speed
        if self.game.settings.up_key in self.game.input_manager.inputs:
            self.rect.y -= self.max_player_speed
        if self.game.settings.down_key in self.game.input_manager.inputs:
            self.rect.y += self.max_player_speed







