import pygame
import generator_mapy as L
import gracze
import strzelanie as S
import time

ilosc_kratek = [28, 24]
wymiar_kratki = 30

# Zmienilem generator, w folderze mapa_lukasz dodaje wszystkie moje pliki

rozdzielczosc = ilosc_kratek[0]*wymiar_kratki, ilosc_kratek[1]*wymiar_kratki
fps = 60
ekran = pygame.display.set_mode(rozdzielczosc)
gracz = gracze.Gracz(nazwa="ziomek", pole_widzenia=10, druzyna=None, punkty_zycia=100, pancerz=0, predkosc=2)
enemy = gracze.Gracz(nazwa = "test", pole_widzenia = 5, druzyna = None, punkty_zycia = 50, pancerz = 0, predkosc = 2)
gracze = pygame.sprite.Group(gracz)
gracze.add(enemy)
Zegarek = pygame.time.Clock()
mapa = L.mapa(ilosc_kratek[0], ilosc_kratek[1], 30, (2, 2, 3, 2))
sciany=mapa.grupa_scian()
lista_pociskow =pygame.sprite.Group()
wszystkie_elementy = pygame.sprite.Group()
deltaczas = 0

dziala=True
while dziala:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dziala=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: dziala = False
        #strzał
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            dmg,bullet=S.oddaj_strzal(gracz.get_kat(),gracz.rect.center[0],gracz.rect.center[1])
            lista_pociskow.add(bullet)
            
    klawisze = pygame.key.get_pressed()
    mapa.rysuj_podloge(ekran)
    lista_pociskow.draw(ekran)
    mapa.rysuj_sciany(ekran)
    lista_pociskow.update()

    for sciana in sciany:
        pygame.sprite.spritecollide(sciana, lista_pociskow, True)
    for bullet in lista_pociskow: 
        if bullet.rect.y < -10 or bullet.rect.x <-10 or bullet.rect.x > rozdzielczosc[0]+10 or bullet.rect.y >rozdzielczosc[1]+10:
            lista_pociskow.remove(bullet)
            #wszystkie_elementy.remove(bullet)
    
    for graczi in gracze:
        graczi.run(sciany = sciany, ekran = ekran,
                   klawisze = klawisze)
    gracze.draw(ekran)
    
    Zegarek.tick(fps)
    pygame.display.flip()
pygame.quit()
