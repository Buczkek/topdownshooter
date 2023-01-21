import labirynt as Generator
import pygame as PG
import math as M


class Block(PG.sprite.Sprite):
    def __init__(self, image, x, y, szerokosc, wysokosc):
       PG.sprite.Sprite.__init__(self)
       self.image = PG.image.load(image)
       self.rect = PG.Rect(x, y, szerokosc, wysokosc)
       self.x = x
       self.y = y
       self._kat = 0
       
    def get_rect(self):
        return self.rect

class mapa:
    def __init__(self, wysokosc, szerokosc, rozmiar_kratki, wielkosci_drzwi):
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc
        self.mapa = Generator.create_world(self.szerokosc, self.wysokosc, 2, wielkosci_drzwi)
        self.rozmiar_kratki = rozmiar_kratki
        self.ziemia_grafika = "Graphics/dirt_30.gif"
        self.sciana_grafika = "Graphics/wall_30.gif"
        self.sciany = PG.sprite.Group()
        self.podlogi = PG.sprite.Group()
        for i in range(self.wysokosc):
            for j in range(self.szerokosc):
                if self.mapa[j][i] == 0:
                    self.podlogi.add(Block(self.ziemia_grafika, i*self.rozmiar_kratki, j*self.rozmiar_kratki, self.rozmiar_kratki, self.rozmiar_kratki))
                elif self.mapa[j][i] == 1:
                    self.sciany.add(Block(self.sciana_grafika, i*self.rozmiar_kratki, j*self.rozmiar_kratki, self.rozmiar_kratki, self.rozmiar_kratki))

    def grupa_scian(self):
        return self.sciany
    
    def rysuj_sciany(self, ekran):
        self.sciany.draw(ekran)

    def rysuj_podloge(self,ekran):
        self.podlogi.draw(ekran)

    def dodaj_postac(self):
        self.sciany.add()
        
