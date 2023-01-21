from podstawy_przedmiotow import Bron

class Pistolet(Bron):
    def __init__(self):
        super().__init__(nazwa="pukawka",
                       szybkostrzelnosc=69,
                       typ=2
                       )
    def nazwa(self):
        return self._nazwa
