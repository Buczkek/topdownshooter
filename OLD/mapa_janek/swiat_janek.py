from mapa_janek import Mapa
from random import randint

def kier_to_pos(kier):
    # kierunki
    # 0 - góra
    # 1 - lewo
    # 2- dół
    # 3 - prawo
    if kier == 0:
        return (0,-1)
    if kier == 1:
        return (-1,0)
    if kier == 2:
        return (0,1)
    if kier == 3:
        return (1,0)

def dodaj(pos1,pos2): # dodawanie dwóch pozycji
    return pos1[0]+pos2[0],pos1[1]+pos2[1]

def pol_to_kor(pol,a0,b0): # położenie na koordynaty
    return a0+pol[0],b0+pol[1]

class Swiat:
    def __init__(self,roz,w,h,roz_kor):
        self.mapy = {}
        self.mapa_map = []
        self.roz = roz
        self.w = w
        self.h = h
        self.roz_kor = roz_kor

    def gen_swiat(self):
        polozenia = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(-self.roz+1,self.roz):
            for j in range(-self.roz+1,self.roz):
                a,b = pol_to_kor((i,j),self.roz-1,self.roz-1)
                if self.mapa_map[b][a] == 1:
                    #sprawdzam czy dookoła są jakieś mapy i zapisuje ich położenie
                    sasiedzi = polozenia.copy()
                    b = 0
                    while b < len(sasiedzi):
                        if dodaj((i,j),sasiedzi[b]) not in self.mapy:
                            sasiedzi.pop(b)
                            b -= 1
                        b += 1
                    # nie sprawdzam dla dołu i prawej bo tam nie ma jeszcze wyrenderowanych map
                    test1 = False
                    test2 = False
                    # na chama generuje mapy dopóki nie bedzie przejść
                    # zapamiętuje współrzędne wyjść
                    while not test1 or not test2:
                        test1 = False
                        test2 = False
                        wyjscia_1 = []
                        wyjscia_2 = []
                        mapa = Mapa(self.w,self.h,self.roz_kor)
                        mapa.gen_cala()
                        if (0,-1) in sasiedzi: # góra
                            for w1 in mapa.wyjscia_gora:
                                if w1[0] in list(map(lambda x : x[0], self.mapy[dodaj((i,j),(0,-1))].wyjscia_dol)):
                                    test1 = True
                                    wyjscia_1.append(w1)
                                    wyjscia_2.append((w1[0],self.h-1))
                        else:
                            test1 = True
                        if (-1,0) in sasiedzi: # lewo
                            for w1 in mapa.wyjscia_lewo:
                                if w1[1] in list(map(lambda x : x[1], self.mapy[dodaj((i,j),(-1,0))].wyjscia_prawo)):
                                    test2 = True
                                    wyjscia_1.append(w1)
                                    wyjscia_2.append((self.w-1,w1[1]))
                        else:
                            test2 = True
                    # teraz są odlepiane wyjścia które pasują

                    # wyjscia na obecnej mapie
                    for g in wyjscia_1:
                        if g[1] == 0:
                            for h in range(self.roz_kor):
                                mapa.mapa[0][g[0]+h] = 0
                        if g[0] == 0:
                            for h in range(self.roz_kor):
                                mapa.mapa[g[1]+h][0] = 0
                    # wyjscia na mapach przylegających
                    for g in wyjscia_2:
                        if g[1] == self.h-1:
                            for h in range(self.roz_kor):
                                self.mapy[dodaj((i,j),(0,-1))].mapa[self.h-1][g[0]+h] = 0
                        if g[0] == self.w-1:
                            for h in range(self.roz_kor):
                                self.mapy[dodaj((i,j),(-1,0))].mapa[g[1]+h][self.w-1] = 0
                    self.mapy[(i,j)] = mapa
                
    def gen_mapy_map(self):
        self.mapa_map = []
        roz = self.roz
        for i in range(2*self.roz):
            self.mapa_map.append([0]*2*self.roz)
        a = self.roz - 1
        b = self.roz - 1
        self.mapa_map[b][a] = 1
        kierunki = list(map(lambda x: kier_to_pos(randint(0,3)), [0]*3))
        roz -= 1
        for i in kierunki:
            c,d = dodaj((a,b),i)
            if self.mapa_map[d][c] != 1:
                self.mapa_map[d][c] = 1
                roz -= 1
                self.rek_do_mapy_map(c,d,roz)
        
    def rek_do_mapy_map(self,a,b,roz):
        kierunki = list(map(lambda x: kier_to_pos(randint(0,3)), [0]*3))
        for i in kierunki:
            c,d = dodaj((a,b),i)
            if c >= 0 and d >= 0 and c < len(self.mapa_map) and d < len(self.mapa_map) and self.mapa_map[d][c] != 1 and roz > 0:
                self.mapa_map[d][c] = 1
                roz -= 1
                #self.rek_do_mapy_map(c,d,roz)
                roz = self.rek_do_mapy_map(c,d,roz) 
        #return
        return roz
        # dzięki tym zmianom w kodzie robi się trochę "chudsza" mapa
        # nie wiem w sumie co lepiej wygląda więc na razie tak zostaje

    def show_mapa_map(self):
        for i in self.mapa_map:
            for j in i:
                if j != 0:
                    print("▓",end="")
                else:
                    print(" ",end="")
            print()

    def get_mapa(self,pos):
        return self.mapy[pos].get_mapa()

    def czy_nalezy(self,pos):
        return pos in self.mapy
    
#test = Swiat(10,40,20,3)
#test.gen_mapy_map()
#test.show_mapa_map()
#test.gen_swiat()
#print(test.mapy)
#print(len(test.mapy))
