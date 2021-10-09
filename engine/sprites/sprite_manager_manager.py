import pygame


class Sprite_Manager_Manager():
    def __init__(self, game):
        print("Sprite Manager Manager Initialized")


        self.game = game
        self.bottom_sprite_group = pygame.sprite.Group()
        self.mid_sprite_group = pygame.sprite.Group()
        self.top_sprite_group = pygame.sprite.Group()
        self.bg_top_group = pygame.sprite.Group()
        self.bg_bottom_group = pygame.sprite.Group()
        self.wg_top_group = pygame.sprite.Group()
        self.wg_bottom_group = pygame.sprite.Group()



        self.groups = [
        self.bottom_sprite_group,
        self.mid_sprite_group,
        self.top_sprite_group,
        self.bg_top_group,
        self.bg_bottom_group,
        self.wg_top_group,
        self.wg_bottom_group]

    def update(self):
        group_index = 0
        for group in self.groups:
            group.update()
            group.draw(self.game.display_manager.surfs[group_index])
            group_index += 1

