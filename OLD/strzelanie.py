import pygame as P
import math
import random

"""klasy"""      

class Bullet(P.sprite.Sprite):
    def __init__(self,angle):
        super().__init__()
##        self.image = P.Surface([4, 10])
##        self.image.fill((255,255,255))
        self.image = P.image.load("img/pocisk.png")
##        self.image.set_alpha(255)
        self.rect = self.image.get_rect()
        self.angle=angle
        self.vol=5
        self.dmg=20
        
    def update(self):
        #wyliczanie trasy
        x=self.vol*math.sin(math.radians(self.angle))
        y=self.vol*math.cos(math.radians(self.angle))
        self.rect.y -= y
        self.rect.x += x
        #print(self.rect)

def punkt_po_koncie(angle,x,y,p_x,p_y):
    angle-=90
    if angle<0:
        angle=360+angle
    
    angle=math.radians(angle)
    x=p_x+(x-p_x)*math.cos(angle)-(y-p_y)*math.sin(angle)
    y=p_y+(x-p_x)*math.sin(angle)+(y-p_y)*math.cos(angle)
    return x,y

def oddaj_strzal(angle,x,y):
    angle=90-angle#+random.randint(-5,5)
    bullet=Bullet(angle)
    x,y=punkt_po_koncie(angle,x+7,y+7,x,y)
    #print(x,y)
    bullet.rect.x = x
    bullet.rect.y = y
    bullet.image=P.transform.rotate(bullet.image,-angle)
    return bullet.dmg,bullet
   
class Player(P.sprite.Sprite):
    #gracz - klasa tymczasowa
    def __init__(self):
        super().__init__()
        self.image = P.Surface([20, 20])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        
    def update(self):
        #poruszanie graczem
        pos = P.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

##"""dane"""
##
##P.init()
##
##screen=500,500 #wymiary do zmiany
##game_display=P.display.set_mode(screen)
##
##clock = P.time.Clock()
##
###lista wszystkich obiektów
##all_sprites_list = P.sprite.Group()
##
###lista scian
##wall_list = P.sprite.Group()
##
###lista pocisków
##bullet_list = P.sprite.Group()
##
###tworzenie gracza
##player = Player()
##all_sprites_list.add(player)
##
###początkowe parametry gracza - pózniej narzucane przez inne programy
##player.rect.y=150
##player.rect.x=150
##player_angle=45
##
##running=True
##
##"""główna pętla"""
##
##while running:
##    for event in P.event.get():
##        #print(event)
##        if event.type == P.QUIT:
##            running = False
##        #strzał
##        if event.type == P.MOUSEBUTTONDOWN and event.button==1:
##            bullet = Bullet(player_angle)
##            print(player_angle)
##            bullet.rect.x = player.rect.x
##            bullet.rect.y = player.rect.y
##            bullet.image=P.transform.rotozoom(bullet.image,90-player_angle,1)
##            all_sprites_list.add(bullet)
##            bullet_list.add(bullet)
##        #opcja testowa
##        if event.type== P.KEYDOWN:
##            if event.key == P.K_e:
##                player_angle+=1
##            if event.key == P.K_q:
##                player_angle-=1
##        
##
##    #poruszanie się ruchomych obiektów
##    all_sprites_list.update()
##    #print(all_sprites_list)
##    #sprawdzanie kolizji
##    for bullet in bullet_list:
##        block_hit_list = P.sprite.spritecollide(bullet, wall_list, True)
##
##        #usuwanie pocisku po trafieniu
##        for block in block_hit_list:
##            dmg=bullet.dmg
##            bullet_list.remove(bullet)
##            all_sprites_list.remove(bullet)
##
##        #usuwanie pocisku za granicą
##        if bullet.rect.y < -10 or bullet.rect.x <-10 or bullet.rect.x > screen[0]+10 or bullet.rect.y >screen[1]+10:
##            bullet_list.remove(bullet)
##            all_sprites_list.remove(bullet)
##            
##    game_display.fill((255,255,255))
##    all_sprites_list.draw(game_display)
##    P.display.flip()
##    clock.tick(60)
##
##P.quit()
##
##
##
