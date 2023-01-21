
from copy import deepcopy
import pygame as PG
import sys

import generator_mapy as Generator
import players as Postacie

rozmiar_kratki = 30

czarny = (0,     0,   0)
bialy  = (255, 255, 255)

ilosc_kratek = [28, 28]
PG.init()
ekran = PG.display.set_mode((rozmiar_kratki*ilosc_kratek[0], rozmiar_kratki*ilosc_kratek[1]))
ekran.fill(bialy)

przycisk = None
gra_zyje = True

gems = PG.sprite.Group()
wrog = Postacie.Postac(210, 60, 30, 30, 5, "Graphics/test.gif", "wrog")
gracz = Postacie.Postac(210, 210, 30, 30, 10, "Graphics/player_30.gif", "gracz")
mapa = Generator.mapa(ilosc_kratek[0], ilosc_kratek[1], 30)
postacie = [gracz, wrog]
do_narysowania = [mapa, gracz] + postacie

zegar = PG.time.Clock()
while gra_zyje:
    for event in PG.event.get():
        if event.type == PG.QUIT:
            gra_zyje = False
        if event.type == PG.KEYDOWN:
            if event.key == PG.K_w or event.key == PG.K_UP:                 # Sprawdzanie, czy wciśnięto "w"
                gracz.nadaj_predkosc("N")
            if event.key == PG.K_d or event.key == PG.K_RIGHT:               # Sprawdzanie, czy wciśnięto "d"
                gracz.nadaj_predkosc("E")
            if event.key == PG.K_s or event.key == PG.K_DOWN:               # Sprawdzanie, czy wciśnięto "s"
                gracz.nadaj_predkosc("W")
            if event.key == PG.K_a or event.key == PG.K_LEFT:               # Sprawdzanie, czy wciśnięto "a"
                gracz.nadaj_predkosc("S")
        if event.type == PG.KEYUP:
            if event.key in (PG.K_w, PG.K_d, PG.K_s, PG.K_a):
                gracz.ruch_stop()

    for postac in postacie: # Sprawdza kazda postac w postaciach (ludzie, potwory itd)
        test = Postacie.Postac(postac.postac_surf.rect.x + postac.przyspieszenie[0], postac.postac_surf.rect.y + postac.przyspieszenie[1], 30, 30, postac.predkosc, "Graphics/test.gif", "test")
        # ^tutaj tworze kopie aktualnie testowanej postaci i symuluje na niej ruch jaki chce wykonac sprawdzana postac
        kolizje = PG.sprite.spritecollide(test.postac_surf, mapa.sciany, False) # sprawdzam kolizje symulacji ze scianami
        if kolizje == []: # jesli nie ma kolizji, wykonuje ruch prawdziwa postacia
            postac.ruch_start()
        else: # jesli jest, nie wykonuje ruchu
            postac.ruch_stop()
    for rzecz in do_narysowania:
        rzecz.rysuj(ekran)
    PG.display.flip()
    ekran.fill(czarny)
    zegar.tick(30)
        
PG.quit()
