from engine.game_events.event import Event

class Test_Event(Event):
    def play(self, objects):
        print("My man!")

