import pygame
import math
from random import randint
from sklearn.cluster import KMeans
pygame.init()

def hieuhaiso(p1,p2):
    return math.sqrt(((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1])))

def draw_screen():
    screen.fill(background)
    clock.tick(60)
    pygame.draw.rect(screen,black,(50,50,700,500))
    pygame.draw.rect(screen,BACKGROUND_PANEL,(55,55,690,490))
    pygame.draw.rect(screen,black,(800,50,50,50))
    screen.blit(text_plus,(810,50))
    pygame.draw.rect(screen,black,(900,50, 50,50))
    screen.blit(dautru,(910,50))
    text=font.render('K = ' + str(K),True, black)
    screen.blit(text,(1000,50))
    pygame.draw.rect(screen,black,(800,150,150,50))
    screen.blit(text_run,(850,150))
    pygame.draw.rect(screen,black,(800,250,150,50))
    screen.blit(text_random,(810,250))
    pygame.draw.rect(screen,black,(800,450,150,50))
    screen.blit(text_agorithm,(810,450))
    pygame.draw.rect(screen,black,(800,550,150,50))
    screen.blit(text_reset,(840,550))

def draw_mouse(mouse_x, mouse_y):
    if(55<mouse_x<745 and 55<mouse_y<545):
        text_mouse=font_small.render("("+str(mouse_x-55)+","+ str(mouse_y-55)+")", True, black)
        screen.blit(text_mouse,(mouse_x+5,mouse_y))
  
screen = pygame.display.set_mode((1200,700))
runing = True
clock = pygame.time.Clock()
font = pygame.font.SysFont('sans',40)
font_small = pygame.font.SysFont('sans',20)
white = (255,255,255)
black = (0,0,0)
BACKGROUND_PANEL = (249, 255, 230)
background = (214,214,214)
text_plus = font.render('+',True,white)
dautru = font.render('-',True,white)

K = 0
error = 0
points = []
clusters = []
label = []

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (147, 153, 35)
PURPLE = (255,0,255)
SKY = (0,255,255)
ORANGE = (255,125,25)
GRAPE = (100,25,125)
GRASS = (55,155,65)

colors = [RED, GREEN, BLUE, YELLOW, PURPLE, SKY, ORANGE, GRAPE, GRASS]
text_run = font.render("Run", True,white)
text_random = font.render("Random", True, white)
text_agorithm = font.render("Agorithm", True, white)
text_reset = font.render("Reset", True, white)

while runing:
    draw_screen()
    mouse_x,mouse_y=pygame.mouse.get_pos()
    draw_mouse(mouse_x, mouse_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(800<mouse_x<850 and 50<mouse_y<100):
                if(K<8):
                    print("Press K+")
                    K+=1

            if(900<mouse_x<950 and 50<mouse_y<100):
                if K>0 :
                    print("Press K-")
                    K+=-1

            if(55<mouse_x<745 and 55<mouse_y<545):
                label=[]
                point=[mouse_x,mouse_y]
                points.append(point)
                print("in panel")

            if(800<mouse_x<950 and 250<mouse_y<300):
                label = []
                clusters = []
                print("random pressed")
                for i in range(K):
                    cluster = [randint(50,750),randint(50,550)]
                    clusters.append(cluster)

            if(800<mouse_x<950 and 150<mouse_y<200):
                print(" run pressed")
                for point in points:
                    listhieuhaiso = []
                    for cluster in clusters:
                        hieuhaiso_list = []
                        hieuhaiso_list = hieuhaiso(point,cluster)
                        listhieuhaiso.append(hieuhaiso_list)

                    hieuhaiso_min = min(listhieuhaiso)
                    sothu = listhieuhaiso.index(hieuhaiso_min)
                    label.append(sothu)

                for i in range(K):
                    sum_x=0
                    sum_y=0
                    count=0

                    for j in range(len(points)):
                        if label[j]==i:
                            sum_x+=points[j][0]
                            sum_y+=points[j][1]
                            count+=1

                    if count>0:
                        clusters_x=int(sum_x/count)
                        clusters_y=int(sum_y/count)
                        clusters[i]=[clusters_x,clusters_y]

            if(800<mouse_x<950 and 550<mouse_y<600):
                print("Reset pressed")
                K = 0
                points = []
                label = []
                clusters = []

            if(800<mouse_x<950 and 450<mouse_y<500):
                print("agorithm pressed")
                kmeans = KMeans(n_clusters=K).fit(points)
                clusters = kmeans.cluster_centers_
                label = kmeans.predict(points)


    for i in range(len(clusters)):
        pygame.draw.circle(screen,colors[i],(clusters[i][0],clusters[i][1]),10)

    for i in range(len(points)):
        pygame.draw.circle(screen,black,(points[i][0],points[i][1]),6)
        if label == []:
            pygame.draw.circle(screen,white,(points[i][0],points[i][1]),5)
        else:
            pygame.draw.circle(screen,colors[label[i]],(points[i][0],points[i][1]),6)

    error=0
    if label != [] and clusters != []:
        for i in range(len(points)):
            error += hieuhaiso(points[i],clusters[label[i]])
            
    text_error = font.render("Error = "+ str(error),True,black)
    screen.blit(text_error,(810,350))
    pygame.display.flip()
pygame.quit()

