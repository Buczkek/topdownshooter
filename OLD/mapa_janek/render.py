from swiat_janek import Swiat
import pygame,os
from random import randint

class Render_mapa(Swiat):
    def __init__(self,w_mapy,h_mapy,w_ekranu,h_ekranu):
        super().__init__(20,w_mapy,h_mapy,4)
        self.sciany = pygame.sprite.Group()
        self.podloga = pygame.sprite.Group()
        self.widziane = pygame.sprite.Group()
        self.mapa_widziana = pygame.Surface((w_ekranu,h_ekranu))
        # sprites ładuje wszystkie obrazy z folderu img, w kolejności
        self.sprites = list(map(lambda x : pygame.image.load("img/"+x)
                                ,sorted(os.listdir("img"))))
        self.sprite_size = 8 # rozmiar jednego
        self.mapa_cala = pygame.Surface((w_mapy*self.sprite_size,
                                         h_mapy*self.sprite_size))

    def gen_map(self,pos):
        # generuje grupe ścian i podłóg w oparciu o podaną mapę
        # pos -- pozycja gracza
        # np. (0,0) oznacza że jest na mapie startowej
        self.sciany.empty()
        self.podloga.empty()
        mapa = self.get_mapa(pos)
        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                # wybieram randomowo obraz dla każdego sprite'a
                if mapa[i][j] == 1:
                    p = randint(2,4) if randint(0,5)==4 else 1
                else:
                    p = randint(5,8) if randint(0,12)==4 else 0
                # tworze za każdym razem nowego sprite'a i dodaje
                # do odpowiedniej grupy
                jeden = pygame.sprite.Sprite()
                jeden.image = self.sprites[p]
                jeden.rect = jeden.image.get_rect()
                jeden.rect.x = j*8
                jeden.rect.y = i*8
                if mapa[i][j] == 1:
                    self.sciany.add(jeden)
                else:
                    self.podloga.add(jeden)
        # taka naprawdę rysuje w tej chwili całą mapę
        # ale dzieje się to tak rzadko że nie ma znaczenia
        # dla wydajności
        self.podloga.draw(self.mapa_cala)
        self.sciany.draw(self.mapa_cala)

    def gen_mapa_widziana(self,other):
        # generuje już grupę sprite'ów którą gracz widzi
        # funkcja potrzebuje klasy gracz z gracz.py
        # a w szczególności funkcji czy_widzi()
        self.widziane.empty()
        for i in self.sciany.sprites() + self.podloga.sprites():
            if other.czy_widzi((i.rect.x,i.rect.y)):
                # musi tutaj tworzyć nowego sprite'a
                # bo pygame.sprite.Sprite() nie ma funkcji copy() :c
                jeden = pygame.sprite.Sprite()
                jeden.image = i.image
                jeden.rect = jeden.image.get_rect()
                self.widziane.add(jeden)
        # znajduje najmniejsze koordynaty z pośród widzianych i odejmuje
        # tą wartość żeby mapa zaczynała się w punkcie (0,0),
        # a nie np w (30,60)
        min_x = min(list(map(lambda x : x.rect.x, self.widziane.sprites())))
        min_y = min(list(map(lambda x : x.rect.y, self.widziane.sprites())))
        for i in self.widziane.sprites():
            i.rect.x -= min_x
            i.rect.y -= min_y
        # jeśli trzeba to mogę podzielić widziane na podłoge i ściany
        # żeby można było sprawdzać kolizje tylko dla tych w pobliżu

    def render_mapa(self,screen,other):
        # to już rysuje na ostatecznej powierzchni,
        # która tu będzie przekazywana
        # potrzeba znowu klasy gracz
        self.mapa_widziana.fill((0,0,0))
        self.gen_mapa_widziana(other)
        # dodaje odpowiedni wycinek całej mapy do ekranu
        self.mapa_widziana.blit(self.mapa_cala,(0,0),
                                (other.x-other.pole_widzenia,
                                 other.y-other.pole_widzenia,
                                 self.mapa_widziana.get_width(),
                                 self.mapa_widziana.get_height()))
        # jeżeli wymiar mapy widzianej od ekranu końcowego się
        # różnią to należałoby przeskalować
        pygame.transform.scale(self.mapa_widziana,screen.get_size(),screen)
                                 
