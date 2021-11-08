import pygame
import os


class Sprite_Manager(pygame.sprite.Sprite):
    def __init__(self, game, object, assetpath, rect, surface_index):
        super().__init__()
        self.game = game
        self.owning_object = object
        self.group_index = surface_index


        self.spritename = assetpath
        self.spritepath = game.path + r'\assets' + assetpath


        if self.spritename == 'none':
            self.image = None
            self.rect = None

        else:
            self.image = pygame.image.load(self.spritepath)
            self.image = pygame.transform.scale(self.image, (rect[2], rect[3]))

            self.rect = pygame.Rect(rect)
            self.rect.center = (self.rect[2] / 2, self.rect[3] / 2)

            self.game.sprite_manager_manager.groups[self.group_index].add(self)

            self.rect.x = rect[0]
            self.rect.y = rect[1]



    def custom_update(self):
        pass


