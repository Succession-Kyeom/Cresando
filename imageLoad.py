import pygame
from AnimationSprite import AnimationSprite

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

text1 = AnimationSprite(position = (500, 300), images = text_1)
text2 = AnimationSprite(position = (740, 300), images = text_2)
text3 = AnimationSprite(position = (980, 300), images = text_3)
text4 = AnimationSprite(position = (1220, 300), images = text_4)
text = [text1, text2, text3, text4]

allSprite = []
allSprite.append(pygame.sprite.Group(text1))
allSprite.append(pygame.sprite.Group(text2))
allSprite.append(pygame.sprite.Group(text3))
allSprite.append(pygame.sprite.Group(text4))