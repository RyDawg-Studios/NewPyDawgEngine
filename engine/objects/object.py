from engine.sprites.sprite_manager import Sprite_Manager
import pygame

class Object():

    sprite_path = ''
    solid = False
    generateOverlapEvents = True
    checkForCollision = False
    blueprint = None
    def __init__(self, game, args):
        self.game = game
        self.ovr_init()
        self.objectname = args[1]
        self.sprite_manager = Sprite_Manager(game, self, self.sprite_path, args[2], args[3])
        self.rect = self.sprite_manager.rect
        if self.rect != None:
            self.rect.center = self.sprite_manager.rect.center
        self.overlap_info = {"Overlapping" : False, "Objects" : []}



    def update(self):
        self.sprite_manager.custom_update()
        self.ovr_update()
        self.check_overlap()
        #pygame.draw.rect(self.game.display_manager.surfs[2], (255, 255, 255), self.rect)


    def check_overlap(self):
        if self.checkForCollision == True:
            for object in self.game.object_manager.all_objects:
                if object in self.overlap_info["Objects"] and object not in self.game.object_manager.all_objects:
                    self.overlap_info["Objects"].remove(object)

                if self.rect.colliderect(object.rect) and object != self:
                    if object not in self.overlap_info["Objects"]:
                        self.overlap_info["Objects"].append(object)
                        object.ovr_on_overlap()

                if not self.rect.colliderect(object.rect) and object in self.overlap_info['Objects']:
                    self.overlap_info["Objects"].remove(object)




        if len(self.overlap_info["Objects"]) > 0:
            self.overlap_info["Overlapping"] = True
        else:
            self.overlap_info["Overlapping"] = False


        pygame.display.set_caption(str(self.overlap_info))

    def ovr_on_overlap(self):
        pass


    def ovr_update(self): #Overide
        pass

    def ovr_init(self): #Overide
        pass

    def debug(self):
        print("I'm Real!")


    def destroy(self):
        for grp in self.game.sprite_manager_manager.groups:
            if self.sprite_manager in grp:
                grp.remove(self.sprite_manager)
                return

