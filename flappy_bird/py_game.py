import pygame,sys
from pygame.constants import MOUSEMOTION

pygame.init()



screen=pygame.display.set_mode((288,512))   #tạo cửa sổ game
pygame.display.set_caption("angry bird :)))")
fps=pygame.time.Clock()

bg=pygame.image.load('background-day.png').convert()
bg_x=0

floor=pygame.image.load('base.png')
floor_x1=0
floor_x2=288

bird_mid=pygame.image.load('bluebird-midflap.png')
bird_down=pygame.image.load('bluebird-downflap.png')
bird_up=pygame.image.load('bluebird-upflap.png')

bird_rotare=pygame.transform.rotate(bird_down,30)

bird_x=144
bird_y=256
gravity=5

def floor_move(floor,floor_x1,floor_x2):
    screen.blit(floor,(floor_x1,450))
    screen.blit(floor,(floor_x2,450))
    floor_x1-=2
    floor_x2-=2
    if floor_x1<=-288 :
        floor_x1=288
    if floor_x2<=-288:
        floor_x2=288

    return (floor_x1,floor_x2)

running=True

while running:

    fps.tick(240)

    for event in pygame.event.get():

        if event.type==pygame.QUIT:

           running=False
    
    screen.blit(bg,(bg_x,0))
    floor_x1,floor_x2=floor_move(floor,floor_x1,floor_x2)
    screen.blit(bird_rotare,(bird_x,bird_y))
    
    pygame.display.update()

pygame.quit()



