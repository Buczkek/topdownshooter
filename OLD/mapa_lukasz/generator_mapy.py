import labirynt as Generator
import pygame as PG


class Block(PG.sprite.Sprite):
    def __init__(self, grafika, x, y, szerokosc, wysokosc):
       PG.sprite.Sprite.__init__(self)
       self.image = PG.image.load(grafika)
       self.rect = PG.Rect(x, y, szerokosc, wysokosc)
       
    def get_rect(self):
        return self.rect

class mapa:
    def __init__(self, wysokosc, szerokosc, rozmiar_kratki):
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc
        self.mapa = Generator.create_world(self.szerokosc, self.wysokosc, 2)
        self.rozmiar_kratki = rozmiar_kratki
        self.ziemia_grafika = "Graphics/dirt_30.gif"
        self.sciana_grafika = "Graphics/wall_30.gif"
        self.sciany = PG.sprite.Group()
        self.podlogi = PG.sprite.Group()
        for i in range(self.wysokosc):
            for j in range(self.szerokosc):
                if self.mapa[i][j] == 0:
                    self.podlogi.add(Block(self.ziemia_grafika, i*self.rozmiar_kratki, j*self.rozmiar_kratki, self.rozmiar_kratki, self.rozmiar_kratki))
                elif self.mapa[i][j] == 1:
                    self.sciany.add(Block(self.sciana_grafika, i*self.rozmiar_kratki, j*self.rozmiar_kratki, self.rozmiar_kratki, self.rozmiar_kratki))

    def grupa_scian(self):
        return self.sciany
    
    def rysuj(self, ekran):
        self.sciany.draw(ekran)
        self.podlogi.draw(ekran)
