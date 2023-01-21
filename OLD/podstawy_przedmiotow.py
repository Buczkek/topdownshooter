class Przedmiot:
    def __init__(self,
                 nazwa = "niezdefiniowana"):
        self._nazwa = nazwa

class Bron(Przedmiot):
    def __init__(self,
                 nazwa,
                 szybkostrzelnosc,
                 typ, # 1 lub 2 (długa/krótka)
                 ):
        super().__init__(nazwa=nazwa)
        self._szybkostrzelnosc = szybkostrzelnosc
        self._typ = typ
        
