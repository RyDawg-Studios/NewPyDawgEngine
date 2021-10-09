class Player_Controller():
    def __init__(self, game, player):
        print("Player Controller Initialized")
        self.game = game
        self.player = player


    def update(self):
        self.player.update()