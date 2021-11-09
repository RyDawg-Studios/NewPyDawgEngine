from engine.objects.object import Object
import pygame


class Player(Object):
    def ovr_init(self):
        print("Player Spawned")
        self.max_player_speed = 3
        self.checkForCollision = True
        self.spritepath = r'\img\icon\thedawg.jpg'

    def ovr_update(self):
        self.update_velocity()

    def update_velocity(self):
        if self.game.settings.right_key in self.game.input_manager.key_inputs:
            self.rect.x += self.max_player_speed
        if self.game.settings.left_key in self.game.input_manager.key_inputs:
            self.rect.x -= self.max_player_speed
        if self.game.settings.up_key in self.game.input_manager.key_inputs:
            self.rect.y -= self.max_player_speed
        if self.game.settings.down_key in self.game.input_manager.key_inputs:
            self.rect.y += self.max_player_speed
