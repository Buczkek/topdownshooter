class Wrog:
    def __init__(self, x, y, pole_widzenia):
        self.x = x
        self.y = y
        self.pole_widzenia = pole_widzenia
        self.spr = None
        self.ruch_now = [0, 0]
        
    def pos(self):
        return self.x, self.y

    def ruch(self, pos):
        self.x += pos[0]
        self.y += pos[1]

    def rusz(self):
        self.ruch(self.ruch_now)

    def start_ruch(self, pos):
        self.ruch_now[0] += pos[0]
        self.ruch_now[1] += pos[1]

    def stop_ruch(self, pos):
        self.ruch_now[0] -= pos[0]
        self.ruch_now[1] -= pos[1]
    
    def czy_widzi(self, pos):
        x, y = pos
        if (x-self.x)**2 + (y-self.y)**2 < self.pole_widzenia**2: # koło
            return True
        return False
