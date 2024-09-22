import pygame
from AnimationSprite import AnimationSprite

#첫 번째 글자
text_1 = []
text_1.append(pygame.image.load('source/image/blind.png'))
text_1.append(pygame.image.load('source/image/text1/크.png'))
text_1.append(pygame.image.load('source/image/text1/그.png'))
text_1.append(pygame.image.load('source/image/text1/구.png'))

#두 번째
text_2 = []
text_2.append(pygame.image.load('source/image/blind.png'))
text_2.append(pygame.image.load('source/image/text2/레.png'))
text_2.append(pygame.image.load('source/image/text2/루.png'))
text_2.append(pygame.image.load('source/image/text2/라.png'))
text_2.append(pygame.image.load('source/image/text2/린.png'))

#세 번째 글자
text_3 = []
text_3.append(pygame.image.load('source/image/blind.png'))
text_3.append(pygame.image.load('source/image/text3/산.png'))
text_3.append(pygame.image.load('source/image/text3/시.png'))
text_3.append(pygame.image.load('source/image/text3/신.png'))
text_3.append(pygame.image.load('source/image/text3/수.png'))

#네 번째 글자
text_4 = []
text_4.append(pygame.image.load('source/image/blind.png'))
text_4.append(pygame.image.load('source/image/text4/도.png'))
text_4.append(pygame.image.load('source/image/text4/소.png'))
text_4.append(pygame.image.load('source/image/text4/보.png'))
text_4.append(pygame.image.load('source/image/text4/수.png'))
text_4.append(pygame.image.load('source/image/text4/구.png'))
text_4.append(pygame.image.load('source/image/text4/조.png'))
text_4.append(pygame.image.load('source/image/text4/코.png'))

text1 = AnimationSprite(position = (460, 560), images = text_1, size = (190, 190), animationTime = 0.6)
text2 = AnimationSprite(position = (706, 560), images = text_2, size = (190, 190), animationTime = 0.6)
text3 = AnimationSprite(position = (951, 560), images = text_3, size = (190, 190), animationTime = 0.4)
text4 = AnimationSprite(position = (1195, 560), images = text_4, size = (190, 190), animationTime = 0.2)
text = [text1, text2, text3, text4]

background1 = pygame.image.load('source/image/background.jpg')
background1 = pygame.transform.scale(background1, (1920, 1080))
background2 = pygame.image.load('source/image/background.jpg')
background2 = pygame.transform.scale(background2, (1920, 1080))

bus = pygame.image.load('source/image/bus.png')
bus = pygame.transform.scale(bus, (1304, 532))

#1600, 200
quiz = []
quiz.append(pygame.image.load('source/image/quiz/quiz_1.png'))
quiz.append(pygame.image.load('source/image/quiz/quiz_2.png'))
quiz.append(pygame.image.load('source/image/quiz/quiz_3.png'))
quiz.append(pygame.image.load('source/image/quiz/quiz_4.png'))
for i in range(len(quiz)):
    quiz[i] = pygame.transform.scale(quiz[i], (1600, 200))

allSprite = []
allSprite.append(pygame.sprite.Group(text1))
allSprite.append(pygame.sprite.Group(text2))
allSprite.append(pygame.sprite.Group(text3))
allSprite.append(pygame.sprite.Group(text4))