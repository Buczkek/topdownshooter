import pygame,os,sys
from swiat_janek import Swiat,dodaj
from random import randint
from gracz_do_testow import Gracz
from render import Render_mapa

def wyswietl(renderer,screen,ply):
    renderer.render_mapa(screen,ply)
    screen.blit(ply.spr,((screen.get_width())//2,(screen.get_height())/2))
    pygame.display.flip()
    
pygame.init()
size = width,height = 640,640
screen = pygame.display.set_mode(size)

test = Render_mapa(80,40,200,200)
test.gen_mapy_map()
test.gen_swiat()
now = (0,0)

clock = pygame.time.Clock()

ply = Gracz(0,0,100)
ply.spr = list(map(lambda x : pygame.image.load("img/"+x), sorted(os.listdir("img"))))[9]

test.gen_map(now)

wyswietl(test,screen,ply)

while True:
   for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_ESCAPE:
            sys.exit()
         elif event.key == pygame.K_UP:
            if test.czy_nalezy(dodaj(now,(0,-1))):
               now = dodaj(now,(0,-1))
               test.gen_map(now)
         elif event.key == pygame.K_DOWN:
            if test.czy_nalezy(dodaj(now,(0,1))):
               now = dodaj(now,(0,1))
               test.gen_map(now)
         elif event.key == pygame.K_LEFT:
            if test.czy_nalezy(dodaj(now,(-1,0))):
               now = dodaj(now,(-1,0))
               test.gen_map(now)
         elif event.key == pygame.K_RIGHT:
            if test.czy_nalezy(dodaj(now,(1,0))):
               now = dodaj(now,(1,0))
               test.gen_map(now)
         elif event.key == pygame.K_w:
            ply.start_ruch((0,-1))
         elif event.key == pygame.K_s:
            ply.start_ruch((0,1))
         elif event.key == pygame.K_a:
            ply.start_ruch((-1,0))
         elif event.key == pygame.K_d:
            ply.start_ruch((1,0))
      if event.type == pygame.KEYUP:
         if event.key == pygame.K_w:
            ply.stop_ruch((0,-1))
         elif event.key == pygame.K_s:
            ply.stop_ruch((0,1))
         elif event.key == pygame.K_a:
            ply.stop_ruch((-1,0))
         elif event.key == pygame.K_d:
            ply.stop_ruch((1,0))
   wyswietl(test,screen,ply)
   ply.rusz()
   clock.tick(30)
