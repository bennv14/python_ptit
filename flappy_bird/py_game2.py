import pygame,sys,random


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
            self.position_1=288
        
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
            self.position_1=288
        
        if self.position_2<=-288:
            self.position_2=288
        

class bird:
    bird_pain=None
    bird_down=None
    bird_mid=None
    bird_up=None
    gravity=0.4
    speed=0
    rotaion=0
    bird_rect=None

    def __init__(self) -> None:
        pass
    
    def move(self):
        #tốc độ dơi
        self.speed+=self.gravity
        self.bird_rect.y+=self.speed
        if self.bird_rect.y>600:
            self.bird_rect.y=600

        #hướng di chuyển
        self.bird_pain=pygame.transform.rotate(self.bird_mid ,self.rotaion)
        self.rotaion-=3
        if self.rotaion<=-70:
            self.rotaion=-70

pipe_height=[130,130,130]

def create_pipe():
    height=random.choice(pipe_height)
    bottom = Pipe1.get_rect(topleft = (300,height))
    top = Pipe2.get_rect(topleft = (300,height-450))
    return top,bottom 
        
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -=5

    if len(pipes)>6:
        del pipes[:2]

    return pipes

def draw_pipe(pipes_top,pipes_bottom):
    for pipe in pipes_top:
        screen.blit(Pipe2,pipe)
    for pipe in pipes_bottom:
        screen.blit(Pipe1,pipe)

bg=background()
bg.background=pygame.image.load('background-day.png')

f=floor()
f.Floor=pygame.image.load('base.png')

screen=pygame.display.set_mode((288,512))
pygame.display.set_caption('haizz làm lúc chán')

#khởi tạo bird
b=bird()
b.bird_mid=pygame.image.load('bluebird-midflap.png')
b.bird_down=pygame.image.load('bluebird-downflap.png')
b.bird_up=pygame.image.load('bluebird-upflap.png')
b.bird_pain=b.bird_mid
b.bird_rect=b.bird_pain.get_rect(topleft = (70,260))

#khởi tạo pipe
pipes_top=[]
pipes_bottom=[]
Pipe1=pygame.image.load('pipe-green.png')
Pipe2=pygame.transform.rotate(Pipe1,180)
pipe_list=[]
SPAWMPIPE =pygame.USEREVENT
pygame.time.set_timer(SPAWMPIPE,900)

rect=Pipe1.get_rect(topleft =(400,150))

time=0
running=True
while running:

    pygame.time.Clock().tick(120)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                b.speed=0
                b.speed-=10
                b.rotaion=60
        elif event.type==SPAWMPIPE:
            a,b=create_pipe()
            pipes_top.append(a)
            pipes_bottom.append(b)
            print(pipe_list)
               

    #tạo background cho game
    screen.blit(bg.background,(bg.position_1,0))
    screen.blit(bg.background,(bg.position_2,0))
    bg.update()

    #tao bird
    screen.blit(b.bird_pain,b.bird_rect)
    b.move()
    
    #tạo pipe
    pipe_list=move_pipes(pipe_list)
    draw_pipe(pipes_top,pipes_bottom)
    

    #tạo nên đất cho game
    screen.blit(f.Floor,(f.position_1,420))
    screen.blit(f.Floor,(f.position_2,420))
    f.update()

    time+=1
    pygame.display.update()




