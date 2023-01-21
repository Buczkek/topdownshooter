from random import randint

def pole(pos1,pos2):
    return (pos2[0]-pos1[0])*(pos2[1]-pos1[1])

class Mapa:
    def __init__(self,w,h,roz_kor):
        self.w = w
        self.h = h
        self.roz_kor = roz_kor
        self.mapa = []
        self.wyjscia_lewo = []
        self.wyjscia_prawo = []
        self.wyjscia_gora = []
        self.wyjscia_dol = []
        
    def gen_kor(self,pos_pocz,pos_kon):
        # sprawdza czy nowy pokój ma wystarczająco małe pole czy trzeba go może podzielić
        if pole(pos_pocz,pos_kon) <= 128:
            self.gen_pok(pos_pocz,pos_kon)
            return
        height = pos_kon[1] - pos_pocz[1]
        width = pos_kon[0] - pos_pocz[0]
        # jeżeli pokój ma większą szerokość niż wysokość to rysuje korytarz góra-dól
        # w przeciwnym wypadku rysuje korytarz lewo-prawo
        if width/2 >= height: # dzielenie przez 2 jest tylko przez to że znaki w terminalu są prostokątne
            # losuje korytarz góra-dół, te wszystkie "+1" są po to żeby korytarz nie był na brzegu pokoju
            if pos_pocz[0] + 1 >= pos_kon[0] - self.roz_kor - 1:
                return
            wsp_kor = randint(pos_pocz[0] + 1, pos_kon[0] - self.roz_kor - 1)
            for i in range(pos_pocz[1],pos_kon[1]):
                for j in range(self.roz_kor):
                    self.mapa[i][wsp_kor + j] = 0
            # rekurencyjnie dzieli pokoje podzielone przez korytarz na inne pokoje
            self.gen_kor(pos_pocz,(wsp_kor,pos_kon[1]))
            self.gen_kor((wsp_kor + self.roz_kor, pos_pocz[1]),pos_kon)
        else:
            if pos_pocz[1] + 1 >= pos_kon[1] - self.roz_kor - 1:
                return
            wsp_kor = randint(pos_pocz[1] + 1, pos_kon[1] - self.roz_kor - 1)
            for i in range(pos_pocz[0],pos_kon[0]):
                for j in range(self.roz_kor):
                    self.mapa[wsp_kor + j][i] = 0
            # oddaje dwa podzielone fragmenty przez korytarz do rekurencji
            self.gen_kor(pos_pocz,(pos_kon[0],wsp_kor))
            self.gen_kor((pos_pocz[0],wsp_kor + self.roz_kor),pos_kon)

    def gen_pok(self,pos_pocz,pos_kon):
        height = pos_kon[1] - pos_pocz[1]
        width = pos_kon[0] - pos_pocz[0]
        if height < 3 or width < 3:
            return
        for i in range(pos_pocz[1] + 1,pos_kon[1] - 1):
            for j in range(pos_pocz[0] + 1,pos_kon[0] - 1):
                self.mapa[i][j] = 0
        pos_kon = (pos_kon[0] - 1, pos_kon[1] - 1)
        # generowanie wyjść jeżeli pokój nie jest na brzegu mapy
        if pos_pocz[1] != 0:
            self.mapa[pos_pocz[1]][randint(pos_pocz[0] + 1,pos_kon[0] - 1)] = 0 # góra
        if pos_kon[1] != self.h - 1: 
            self.mapa[pos_kon[1]][randint(pos_pocz[0] + 1,pos_kon[0] - 1)] = 0 # dół
        if pos_pocz[0] != 0:
            self.mapa[randint(pos_pocz[1] + 1,pos_kon[1] - 1)][pos_pocz[0]] = 0 # lewo
        if pos_kon[0] != self.w - 1: 
            self.mapa[randint(pos_pocz[1] + 1,pos_kon[1] - 1)][pos_kon[0]] = 0 # prawo
                
    def gen_mapa(self):
        self.mapa = []
        for i in range(self.h):
            self.mapa.append([1]*self.w)
        self.gen_kor((0,0),(self.w,self.h))
                   
    def szuk_wyjsc(self):
        for i in range(1,self.w):
            # góra
            if self.mapa[0][i] == 0 and self.mapa[0][i-1] != 0:
                self.wyjscia_gora.append((i,0))
            # dół
            if self.mapa[self.h-1][i] == 0 and self.mapa[self.h-1][i-1] != 0:
                self.wyjscia_dol.append((i,self.h-1))
        for i in range(1,self.h):
            # lewo
            if self.mapa[i][0] == 0 and self.mapa[i-1][0] != 0:
                self.wyjscia_lewo.append((0,i))
            # prawo
            if self.mapa[i][self.w-1] == 0 and self.mapa[i-1][self.w-1] != 0:
                self.wyjscia_prawo.append((self.w-1,i))
        # teraz dzieje się naprawa wyjść lewo-prawo
        if len(self.wyjscia_lewo) == 0:
            wyj = randint(1,self.h-self.roz_kor-1)
            self.wyjscia_lewo.append((0,wyj))
        if len(self.wyjscia_prawo) == 0:
            wyj = randint(1,self.h-self.roz_kor-1)
            self.wyjscia_prawo.append((self.w-1,wyj))

    def gen_cala(self):
        self.gen_mapa()
        self.szuk_wyjsc()
        # zalepiam wszystkie wyjścia, będę je otwierał dopiero jak uda mi się wykryć ktróre pasują do świata
        zjebanie = [0]*4
        for i in range(self.w):
            self.mapa[0][i] = 1
            self.mapa[self.h-1][i] = 1
            if self.mapa[1][i] == 1:
                zjebanie[0] += 1
            if self.mapa[self.h-2][i] == 1:
                zjebanie[1] += 1
        for i in range(self.h):
            self.mapa[i][0] = 1
            self.mapa[i][self.w-1] = 1
            if self.mapa[i][1] == 1:
                zjebanie[2] += 1
            if self.mapa[i][self.w-2] == 1:
                zjebanie[3] += 1
        # teraz dzieje się naprawa tego że czasami wyjścia się generują w pustce
        # w pętli powyżej szukamy, która ściana jest zjebana
        if zjebanie[0] == self.w:
            for i in range(1,self.w-1):
                self.mapa[1][i] = 0
        
        if zjebanie[1] == self.w:
            for i in range(1,self.w-1):
                self.mapa[self.h-2][i] = 0

        if zjebanie[2] == self.h:
            for i in range(1,self.h-1):
                self.mapa[i][1] = 0

        if zjebanie[3] == self.h:
            for i in range(1,self.h-1):
                self.mapa[i][self.w-2] = 0


    def show(self):
        for i in self.mapa:
            for j in i:
                if j == 0:
                    print(" ",end="")
                else:
                    print("▓",end="")
            print()
            
    def get_mapa(self):
        return self.mapa
#test = Mapa(100,20,4)
#test.gen_mapa()
#test.szuk_wyjsc()
#test.show()
