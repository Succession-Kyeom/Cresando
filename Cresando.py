import pygame
import time
import sys
import os
from imageLoad import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)

size = (1920, 1080) #화면 사이즈
screen = pygame.display.set_mode(size)
cresandoIcon = pygame.image.load('source/image/CresandoMark.ico') #크레산도 아이콘
pygame.display.set_caption("Cresando") #프로그램명
pygame.display.set_icon(cresandoIcon) #화면 상단 아이콘

clock = pygame.time.Clock()
fps = 60

roop = True
index = 0
control = True
hard = False
quizIndex = 0
keyR = 0
keyU = 0
keyA = 0
speed = 3

background1_x = 0
background2_x = 1920


pygame.init()
pygame.mixer.init()

correct = pygame.mixer.Sound('source/sound/correct.wav')
wrong = pygame.mixer.Sound('source/sound/wrong.wav')

correct.set_volume(0.3)
wrong.set_volume(0.3)

def stop(index):
    if index < len(text):
        text[index].isSpin = False
        if (index + 1) < len(text):
            text[index + 1].blind = False
        index += 1
    return index

def IsCorrect():
    global correct
    global wrong

    for i in range(len(text)):
        if text[i].index != 1:
            wrong.play()
            return
    correct.play()
    return

def init():
    global control
    global index
    global text
    global hard
    global keyR
    global keyU
    global keyA

    control = False
    index = 0
    for i in range(len(text)):
        text[i].isSpin = True
        text[i].blind = True
    text[0].blind = False
    control = True
    hard = False
    keyR = 0
    keyU = 0
    keyA = 0
    return

init()
#메인 루프
while roop:
    mt = clock.tick(fps) / 1000
    if quizIndex == 4:
        quizIndex = 0

    # 배경화면 설정
    screen.blit(background1, [background1_x, 0])
    screen.blit(background2, [background2_x, 0])
    screen.blit(quiz[quizIndex], (160, 70))
    screen.blit(bus, (350, 450))

    background1_x -= speed
    background2_x -= speed
    if background1_x <= -1920:
        background1_x = 1920
    elif background2_x <= -1920:
        background2_x = 1920

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           roop = False
        if event.type == pygame.KEYDOWN and control == True:
            if event.key == pygame.K_SPACE:
                index = stop(index)
            elif event.key == pygame.K_r:
                keyR = 1
                if keyA == 1:
                    keyR = 2
            elif event.key == pygame.K_u and keyR != 0:
                keyU = 1
                if keyR == 2:
                    keyU = 2
            elif event.key == pygame.K_a and keyU != 0:
                keyA = 1
                if keyU == 2:
                    keyA = 2
            elif event.key == pygame.K_RETURN and keyR == 2 and keyU == 2 and keyA == 2:
                for i in range(len(text)):
                    text[i].animationTime = 0.1
                speed = 40
            elif event.key == pygame.K_ESCAPE:
                init()

    if index >= len(text):
        control = False
        IsCorrect() #정답 여부 확인
        time.sleep(3)
        init()
        quizIndex += 1

    for i in range(len(allSprite)):
        allSprite[i].update(mt)
        allSprite[i].draw(screen)

    pygame.display.update()

pygame.quit()