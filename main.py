import pygame
import time

size = (1920, 1080) #화면 사이즈
screen = pygame.display.set_mode(size)
cresandoIcon = pygame.image.load('image/CresandoMark.jpg') #크레산도 아이콘
pygame.display.set_caption("Cresando") #프로그램명
pygame.display.set_icon(cresandoIcon) #화면 상단 아이콘
background = (255, 255, 255) #배경 색상

clock = pygame.time.Clock()
fps = 60

class AnimationSprite(pygame.sprite.Sprite):
    def __init__(self, position, images):
        super(AnimationSprite, self).__init__()

        size = (100, 100) #이미지 사이즈

        #이미지 사이즈 맞추기
        self.rect = pygame.Rect(position, size)
        self.images = [pygame.transform.scale(image, size) for image in images]

        #첫번째 이미지
        self.index = 0
        self.image = images[self.index]

        self.animationTime = 0.5 #이미지 사이클 주기
        self.currentTime = 0

        self.isSpin = True

    def update(self, mt):
        if self.isSpin == True:
            self.currentTime += mt

            #currentTime 및 index 초과 시 초기화
            if self.currentTime >= self.animationTime:
                self.currentTime = 0
                self.image = self.images[self.index]

                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0

roop = True
index = 0
control = True

#첫 번째 글자
text_1 = []
text_1.append(pygame.image.load('image/text1/카.png'))
text_1.append(pygame.image.load('image/text1/코.png'))
text_1.append(pygame.image.load('image/text1/쿠.png'))
text_1.append(pygame.image.load('image/text1/크.png'))
text_1.append(pygame.image.load('image/text1/키.png'))

#두 번째
text_2 = []
text_2.append(pygame.image.load('image/text2/라.png'))
text_2.append(pygame.image.load('image/text2/래.png'))
text_2.append(pygame.image.load('image/text2/리.png'))
text_2.append(pygame.image.load('image/text2/레.png'))
text_2.append(pygame.image.load('image/text2/로.png'))

#세 번째 글자
text_3 = []
text_3.append(pygame.image.load('image/text3/산.png'))
text_3.append(pygame.image.load('image/text3/삼.png'))
text_3.append(pygame.image.load('image/text3/선.png'))
text_3.append(pygame.image.load('image/text3/순.png'))
text_3.append(pygame.image.load('image/text3/찬.png'))

#네 번째 글자
text_4 = []
text_4.append(pygame.image.load('image/text4/다.png'))
text_4.append(pygame.image.load('image/text4/대.png'))
text_4.append(pygame.image.load('image/text4/더.png'))
text_4.append(pygame.image.load('image/text4/도.png'))
text_4.append(pygame.image.load('image/text4/두.png'))

text1 = AnimationSprite(position = (200, 100), images = text_1)
text2 = AnimationSprite(position = (460, 100), images = text_2)
text3 = AnimationSprite(position = (720, 100), images = text_3)
text4 = AnimationSprite(position = (980, 100), images = text_4)
text = [text1, text2, text3, text4]

allSprite = []
allSprite.append(pygame.sprite.Group(text1))
allSprite.append(pygame.sprite.Group(text2))
allSprite.append(pygame.sprite.Group(text3))
allSprite.append(pygame.sprite.Group(text4))

def stop(index):
    text[index].isSpin = False
    index += 1
    return index

def IsCorrect():
    if text[0].index == 3 and text[1].index == 2 and text[2].index == 0 and text[3].index == 3:
        print('true')
        return True
    else:
        print('false')
        return False

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

    if index >= len(text):
        control = False
        correct = IsCorrect() #정답 여부 확인
        time.sleep(3)
        control = True
        index = 0
        for i in range(len(text)):
            text[i].isSpin = True

    for i in range(len(allSprite)):
        allSprite[i].update(mt)
        allSprite[i].draw(screen)

    pygame.display.update()

pygame.quit()