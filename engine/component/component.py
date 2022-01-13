class Component:
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs['kwargs']
        self.owner = self.kwargs['owner']
        #print("oh yeah, we componenting")

    def update(self):
        pass

    def setowner(self, owner):
        self.owner = owner