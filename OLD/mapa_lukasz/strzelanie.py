import pygame as P
import math

"""klasy"""      

class Bullet(P.sprite.Sprite):
    
    def __init__(self,angle):
        super().__init__()
        self.image = P.Surface([4, 10])
        self.image.fill((255,255,255))
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

"""dane"""

P.init()

screen=500,500 #wymiary do zmiany
game_display=P.display.set_mode(screen)

clock = P.time.Clock()

#lista wszystkich obiektów
all_sprites_list = P.sprite.Group()

#lista scian
wall_list = P.sprite.Group()

#lista pocisków
bullet_list = P.sprite.Group()

#tworzenie gracza
player = Player()
all_sprites_list.add(player)

#początkowe parametry gracza - pózniej narzucane przez inne programy
player.rect.y=150
player.rect.x=150
player_angle=45

running=True

"""główna pętla"""

while running:
    for event in P.event.get():
        #print(event)
        if event.type == P.QUIT:
            running = False
        #strzał
        if event.type == P.MOUSEBUTTONDOWN and event.button==1:
            bullet = Bullet(player_angle)
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            bullet.image=P.transform.rotozoom(bullet.image,-player_angle,1)
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
        #opcja testowa
        if event.type== P.KEYDOWN:
            if event.key == P.K_e:
                player_angle+=5
            if event.key == P.K_q:
                player_angle-=5
        

    #poruszanie się ruchomych obiektów
    all_sprites_list.update()

    #sprawdzanie kolizji
    for bullet in bullet_list:
        block_hit_list = P.sprite.spritecollide(bullet, wall_list, True)

        #usuwanie pocisku po trafieniu
        for block in block_hit_list:
            dmg=bullet.dmg
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

        #usuwanie pocisku za granicą
        if bullet.rect.y < -10 or bullet.rect.x <-10 or bullet.rect.x > screen[0]+10 or bullet.rect.y >screen[1]+10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            
    game_display.fill((0,0,0))
    all_sprites_list.draw(game_display)
    P.display.flip()
    clock.tick(60)

P.quit()
