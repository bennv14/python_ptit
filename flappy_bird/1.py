import pygame
import random
import time
from pygame import event
from pygame.constants import QUIT

def FPS (fps):
    time.sleep(1/fps)

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WIDTH = 600  # width of our game window
HEIGHT = 600 # height of our game window
 # frames per second


screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Game")
pygame.mixer.init()
#pygame.draw.rect(screen, RED,(100, 100, 100, 100))
hinh=pygame.draw
hinh.rect(screen, RED,(50, 100, 100, 100))



running=True

while running:

    FPS(30)# frames per second
    
    for event in pygame.event.get():

        if event.type==pygame.QUIT:

            running=False

   

    pygame.display.flip()

pygame.QUIT
        