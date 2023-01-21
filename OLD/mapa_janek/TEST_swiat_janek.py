import curses
from swiat_janek import Swiat, dodaj

curses.initscr()
curses.noecho()
curses.curs_set(0)
curses.halfdelay(1)

win = curses.newwin(100,200,0,0)

win.keypad(True)

test = Swiat(20,40,20,2)
test.gen_mapy_map()
test.gen_swiat()

now = (0,0)

def wyswietl(mapa,win):
    win.clear()
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 1:
                win.addstr(i,j,"▓")
    win.addstr(3,50,str(now))

wyswietl(test.get_mapa(now),win)

while True:
    c = win.getch()
    if c == curses.KEY_UP:
       if test.czy_nalezy(dodaj(now,(0,-1))):
           now = dodaj(now,(0,-1))
           wyswietl(test.get_mapa(now),win)
    elif c == curses.KEY_DOWN:
       if test.czy_nalezy(dodaj(now,(0,1))):
           now = dodaj(now,(0,1))
           wyswietl(test.get_mapa(now),win)
    elif c == curses.KEY_LEFT:
       if test.czy_nalezy(dodaj(now,(-1,0))):
           now = dodaj(now,(-1,0))
           wyswietl(test.get_mapa(now),win)
    elif c == curses.KEY_RIGHT:
       if test.czy_nalezy(dodaj(now,(1,0))):
           now = dodaj(now,(1,0))
           wyswietl(test.get_mapa(now),win)
    elif c == 27:
        break
    
curses.endwin()
test.show_mapa_map()
