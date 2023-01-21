import pygame
import bronie
import math as M

class Gracz(pygame.sprite.Sprite):
    def __init__(self, nazwa, pancerz, punkty_zycia,  x=50, y=50, pole_widzenia=10,
                 druzyna=None, predkosc = 10):
        super(Gracz,self).__init__()
        self.zmniejszenie_hitboxa = 8 #w pixelach
        self._przesuniecie_hitboxa = self.zmniejszenie_hitboxa // 2
        self._x = x
        self._y = y
        self._pole_widzenia = pole_widzenia
        self._punkty_zycia = punkty_zycia
        self._pancerz = pancerz
        self._predkosc = predkosc
        self._druzyna = druzyna
        self._bron = bronie.Pistolet()
        self._kat = 0

        self.zaladuj_teksture()
        
    def zaladuj_teksture(self):
        if self._bron.nazwa() == "pukawka":
            tekstura = "img/zolnierze/Top_Down_Survivor/handgun/idle/survivor-idle_handgun_0.png"
        self.image = pygame.image.load(tekstura)
        self.image_kopia = self.image
        self.rect = self.image.get_rect()
        self.rect.center = self._x, self._y
        self.dokolizji = pygame.sprite.Sprite()
        rozmiar = self.rect.size
        rozmiar = rozmiar[0] - self.zmniejszenie_hitboxa, rozmiar[1] - self.zmniejszenie_hitboxa
        x, y = self.rect.x+self._przesuniecie_hitboxa, self.rect.y+self._przesuniecie_hitboxa
        self.dokolizji.rect = pygame.Rect((x, y), rozmiar)
    def tekstura(self):
        return self.image
    def pos(self):
        return self._x, self._y
    def zycie(self):
        return self._punkty_zycia
    def pancerz(self):
        return self._pancerz
    def otrzymaj_obrazenia(self, ile):
        if _pancerz != 0:
            if _pancerz < ile:
                _zycie -= ile - _pancerz
                _pancerz = 0
        elif _zycie >= ile: _zycie -= ile
        else: _zycie = 0
        if _zycie == 0: self.smierc()
    def hitbox(self):
        return self.rect
    def ksztalt(self):
        self.hitbox()
    def smierc(self):
        pass
    def ustal_predkosc(self, klawisze):
        predkosc = [0,0]
        w = False
        a = False
##    print(klawisze[pygame.K_w])
##    print(klawisze[pygame.K_w])
        if klawisze[pygame.K_w]:
            predkosc[1] = self._predkosc * (-1)
            w = True
        else:
            predkosc[1] = 0
      
        if klawisze[pygame.K_s]:
            predkosc[1] = self._predkosc
        elif not w:
            predkosc[1] = 0

        if klawisze[pygame.K_a]:
            predkosc[0] = self._predkosc * (-1)
            a = True
        else:
            predkosc[0] = 0
            
        if klawisze[pygame.K_d]:
            predkosc[0] = self._predkosc
        elif not a:
            predkosc[0] = 0
##        print("ustalona",predkosc)
        return predkosc

    def ruch(self,predkosc):
##        self.rect.move(predkosc)
        self.rect.x += predkosc[0]
        self.rect.y += predkosc[1]
##        print("wykonano ruch, predkosc:", predkosc)
        self._x, self._y = self.rect.center
    def obrot(self):
        Mpos = pygame.mouse.get_pos()
        Gpos = self._x, self._y
        x = Mpos[0] - Gpos[0]
        y = Mpos[1] - Gpos[1]
        if y!=0:
            tan = x/y
            rad = M.atan(tan)
            kat = M.degrees(rad) // 1
        elif x>0:
            kat = 0
        else:
            kat = 180
        if Mpos[1] > Gpos[1]:
            kat -= 90
        elif Mpos[1] < Gpos[1]:
            kat+=90
        self.image = pygame.transform.rotate(self.image_kopia, kat)
        self.rect = self.image.get_rect()
        self.rect.center = Gpos
        self._kat = kat

    def czy_widzi(self, pos):
        x,y = pos
        #if (x-self._x)**2 + (y-self._y)**2 < self._pole_widzenia**2: # koło
        if abs(x-self.x) <= self.pole_widzenia and abs(y-self.y) <= self.pole_widzenia: # kwadrat
            return True
        return False

    def get_kat(self):
        return self._kat

##    def rysuj(self, ekran):
##        ekran.blit(self.image, self.rect)
    def czy_kolizja(self, grupa):
        for i in pygame.spritecollide(self, grupa, False):
            return True
        return False
    def kolizje_ze_scianami(self, sciany, predkosc):
        self.dokolizji.rect.x += predkosc[0]
        
        if pygame.sprite.spritecollide(self.dokolizji, sciany, False):
            self.dokolizji.rect.x -= predkosc[0]
            predkosc[0] = 0
            
        self.dokolizji.rect.y += predkosc[1]
        
        if pygame.sprite.spritecollide(self.dokolizji, sciany, False):
            self.dokolizji.rect.y -= predkosc[1]
            predkosc[1] = 0
            
        return predkosc
    
    def czy_strzal(klawisze):
        pass
    def strzal(self, czy_strzelic):
        pass
        
##    def kolizje_z_pociskami(self,pociski):
##        for kolizja in pygame.sprite.spritecollide(self, pociski, True):
##            self.otrzymaj_obrazenia(kolizja.obrazenia())
    def run(self, sciany, ekran, klawisze): #...pociski...
##        self.kolizje_z_pociskami(pociski)
        self._ustalona_predkosc = self.ustal_predkosc(klawisze)
##        print("przekazana",self._ustalona_predkosc)
##        print("przed scianami", self._predkosc)
        self._ustalona_predkosc = self.kolizje_ze_scianami(sciany, self._ustalona_predkosc)
##        print("po scianach", self._predkosc)
        self.ruch(self._ustalona_predkosc)
        self.obrot()
        self.strzal(self.czy_strzal())
##        self.rysuj(ekran)
        
            
        
