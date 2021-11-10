from engine.display.display_manager import DisplayManager
from engine.events.event_manager import EventManager
from engine.events.input.input_manager import InputManager
from engine.sprites.sprite_manager_manager import Sprite_Manager_Manager
from engine.objects.object_manager import Object_Manager
from engine.player.player_controller import Player_Controller
from engine.mouse.mouse_manager import Mouse_Manager
from config.config import Settings_Manager
from engine.levels.level_manager import Level_Manager
from engine.levels.debug.test_level import DemoLevel
from engine.levels.debug.stresstest_level import StressLevel
import pygame

class Game:
    def __init__(self, path):
        print("Game Manager Initialized")

        self.path = path

        self.clock = pygame.time.Clock()


        #initialize managers
        self.event_manager = EventManager(self)
        self.input_manager = InputManager(self)
        self.display_manager = DisplayManager(self)
        self.sprite_manager_manager = Sprite_Manager_Manager(self)
        self.object_manager = Object_Manager(self)
        self.settings = Settings_Manager(self)
        self.level_manager = Level_Manager(self)
        self.mouse_manager = Mouse_Manager(self)


        self.pregameloop()
        self.startgameloop()

    def pregameloop(self):
        self.level_manager.init(DemoLevel(self))
        self.player_manager = Player_Controller(self, self.level_manager.current_level.player)


    def startgameloop(self):
        while True:
            self.game_loop()


    def game_loop(self):
        self.manage_managers()
        self.clock.tick(60)



    def manage_managers(self):
        for event in pygame.event.get():
            self.event_manager.update(event)
        self.sprite_manager_manager.update()
        self.player_manager.update()
        self.level_manager.update()
        self.mouse_manager.update()

        self.display_manager.update()  #This ALWAYS Goes Last in this Function


    def exitgame(self):
        pygame.quit()
        exit()