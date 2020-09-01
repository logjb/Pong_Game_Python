import pygame
import math
import random


class snake(object):
    def __init__(selfself,color,pos):
        pass

    def move(self):
        pass

    def reset(self,pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

class cube(object):
    rows = 0
    width = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

def drawGrid(w,rows,surface):
    sizeBtwn = w/rows

    x = 0
    y = 0

    for i in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    #drawGrid(width, rows, surface)
    pygame.display.update()



def main():
    global width, rows

    width = 500
    rows = 20
    window = pygame.display.set_mode((width, width))
    #snakey = snake((255,0,0), (10,10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        #delay the game every 50 milliseconds
   #     pygame.time.delay(50)
        #limit on FPS
   #     clock.tick(10)
   #     print("redrawing window")
   #     redrawWindow(window)
        pass



main()