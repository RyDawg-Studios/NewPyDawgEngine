class Widget_Manager():
    def __init__(self, game):
        print("Widget Manager Initialized")
        self.active_widgets = []
        self.game = game

    def activate_widget(self, wg):
        self.active_widgets.append(wg)


    def update(self):
        for wg in self.active_widgets:
            wg.update()


