from engine.objects.object import Object
from engine.actions.actions.act_destroy_test import Destroy_Action
import pygame


class Player(Object):
    def ovr_init(self):
        print("Player Spawned")
        self.max_player_speed = 3
        self.checkForCollision = True
        self.sprite_path = r'.\assets\img\icon\thedawg.jpg'
        self.player_state = {"debug": False, "moving": True, "direction": "up"}
        self.player_actions = {"debug": False}

    def ovr_update(self):
        self.update_velocity()
        self.update_state()


    def update_state(self):
        """Update Player_State and Player_Actions"""
        if self.game.settings.debug_key in self.game.input_manager.key_inputs and self.player_actions["debug"] == False:
            self.player_actions["debug"] = True
            self.debug()
        if self.game.settings.debug_key not in self.game.input_manager.key_inputs:
            self.player_actions["debug"] = False


    def update_velocity(self):
        if self.game.settings.right_key in self.game.input_manager.key_inputs:
            self.rect.x += self.max_player_speed
        if self.game.settings.left_key in self.game.input_manager.key_inputs:
            self.rect.x -= self.max_player_speed
        if self.game.settings.up_key in self.game.input_manager.key_inputs:
            self.rect.y -= self.max_player_speed
        if self.game.settings.down_key in self.game.input_manager.key_inputs:
            self.rect.y += self.max_player_speed

    def debug(self):
        act = Destroy_Action(self.game)
        act.play(self.overlap_info["Objects"])
        print("debug")