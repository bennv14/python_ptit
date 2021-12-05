import pygame,sys
from pygame.constants import MOUSEMOTION


pygame.init()

class background:
    background=None
    position_1=0
    position_2=288
    speed=2
    def __init__(self) -> None:
        pass

    def update(self):

        self.position_1-=self.speed
        self.position_2-=self.speed

        if self.position_1<=-288:
            self.potion_1=288
        
        if self.position_2<=-288:
            self.position_2=288

        

class floor:
    Floor=None
    position_1=0
    position_2=288
    speed=2

    def __init__(self) -> None:
        pass

    def update(self):

        self.position_1-=self.speed
        self.position_2-=self.speed

        if self.position_1<=-288:
            self.potion_1=288
        
        if self.position_2<=-288:
            self.position_2=288
        

class bird:
    bird_down=None
    bird_mid=None
    bird_up=None
    gravity=10
    speed=0
    position=256

    def __init__(self) -> None:
        pass

    def move(self):
        self.speed+=self.gravity

        self.position+=self.speed
        return self.position

bg=background()
bg.background=pygame.image.load('background-day.png')

f=floor()
f.Floor=pygame.image.load('base.png')

screen=pygame.display.set_mode((288,512))
pygame.display.set_caption('haizz làm lúc chán')
running=True
while running:

    pygame.time.Clock().tick(240)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    #tạo background cho game
    screen.blit(bg.background,(bg.position_1,0))
    screen.blit(bg.background,(bg.position_2,0))
    bg.update()

    if bg.position_1<=-288:
        bg.position_1=288

    #tạo nên đất cho game
    screen.blit(f.Floor,(f.position_1,450))
    screen.blit(f.Floor,(f.position_2,450))
    f.update()
    if(f.position_1<=-288):
        f.position_1=288
    

    pygame.display.update()




