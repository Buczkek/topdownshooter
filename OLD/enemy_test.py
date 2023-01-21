import pygame as PG

from generator_mapy import Block

class Postac:
    def __init__(self, x, y, szerokosc, wysokosc, predkosc, grafika, nazwa):
        self.postac_surf = Block(grafika, x, y, szerokosc, wysokosc)
        self.postac = PG.sprite.Group()
        self.postac.add(self.postac_surf)
        self.predkosc = predkosc
        self.przyspieszenie = [0, 0]
        self.nazwa = nazwa

        
    def nadaj_predkosc(self, kierunek):
        if kierunek == "N":
            self.przyspieszenie[1] = -self.predkosc
        elif kierunek == "E":
            self.przyspieszenie[0] = self.predkosc
        elif kierunek == "W":
            self.przyspieszenie[1] = self.predkosc
        elif kierunek == "S":
            self.przyspieszenie[0] = -self.predkosc

    def ruch_start(self):
        self.postac_surf.rect.x += self.przyspieszenie[0]
        self.postac_surf.rect.y += self.przyspieszenie[1]
        
    def ruch_stop(self):
        self.przyspieszenie = [0, 0]

    def rysuj(self, ekran):
        self.postac.draw(ekran)
