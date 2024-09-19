import pygame
import time
from imageLoad import *

size = (1920, 1080) #화면 사이즈
screen = pygame.display.set_mode(size)
cresandoIcon = pygame.image.load('image/CresandoMark.jpg') #크레산도 아이콘
pygame.display.set_caption("Cresando") #프로그램명
pygame.display.set_icon(cresandoIcon) #화면 상단 아이콘
background = (255, 255, 255) #배경 색상

clock = pygame.time.Clock()
fps = 60

roop = True
index = 0
control = True

def stop(index):
    text[index].isSpin = False
    index += 1
    return index

def IsCorrect():
    if text[0].index == 4 and text[1].index == 4 and text[2].index == 1 and text[3].index == 4:
        print('true')
        return True
    else:
        print('false')
        return False

def init():
    global control
    global index
    global text

    control = False
    index = 0
    for i in range(len(text)):
        text[i].isSpin = True
    control = True
    return

init()
#메인 루프
while roop:
    mt = clock.tick(fps) / 1000
    screen.fill(background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           roop = False
        if event.type == pygame.KEYDOWN and control == True:
            if event.key == pygame.K_SPACE:
                index = stop(index)
                print("space")
            elif event.key == pygame.K_r:
                init()

    if index >= len(text):
        control = False
        correct = IsCorrect() #정답 여부 확인
        time.sleep(3)
        init()

    for i in range(len(allSprite)):
        allSprite[i].update(mt)
        allSprite[i].draw(screen)

    pygame.display.update()

pygame.quit()