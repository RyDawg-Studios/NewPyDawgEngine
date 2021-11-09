from engine.widgets.widget_manager import Widget_Manager
from engine.widgets.widget import Widget


class Player_Controller():
    def __init__(self, game, player):
        print("Player Controller Initialized")
        self.game = game
        self.player = player
        #self.widget_manager = Widget_Manager(self.game)
        #self.widget_manager.activate_widget(Widget(self.game, r'C:\Users\Administrator\Documents\GitHub\NewPyDawgEngine\engine\widgets\widgets\wg_test.json'))


    def update(self):
        self.player.update()