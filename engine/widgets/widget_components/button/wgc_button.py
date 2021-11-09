from engine.objects.object import Object

class Button(Object):

    button_state = {"Hovered": False, "Pressed": False}

    def __init__(self, game, *args):
        if "Nuts" in args:
            print("Nuts")

    def ovr_update(self):
        if self.rect.collidepoint(self.game.mouse_manager.pos[0], self.game.mouse_manager.pos[1]):
            if not self.button_state["Hovered"]:
                self.ovr_hover()
            self.button_state["Hovered"] = True

        else:
            if self.button_state["Hovered"]:
                self.ovr_unhover()
                self.button_state["Hovered"] = False

        if self.button_state["Hovered"] and self.game.input_manager.mouse_inputs[0]:
            if not self.button_state["Pressed"]:
                self.ovr_clicked()
            self.button_state["Pressed"] = True

        else:
            if self.button_state["Pressed"]:
                self.ovr_unclicked()
                self.button_state["Pressed"] = False


    def ovr_clicked(self):
        pass

    def ovr_unclicked(self):
        pass

    def ovr_hover(self):
        pass

    def ovr_unhover(self):
        pass



