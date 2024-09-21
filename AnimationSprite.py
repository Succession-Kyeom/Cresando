import pygame
import random as rd

class AnimationSprite(pygame.sprite.Sprite):
    def __init__(self, position, images, size, animationTime):
        super(AnimationSprite, self).__init__()

        #이미지 사이즈 맞추기
        self.rect = pygame.Rect(position, size)
        self.images = [pygame.transform.scale(image, size) for image in images]

        #첫번째 이미지
        self.index = 0
        self.image = images[self.index]

        self.animationTime = animationTime
        self.currentTime = 0

        self.isSpin = True
        self.blind = True

    def update(self, mt):
        if self.isSpin == True:
            self.currentTime += mt

            #currentTime 및 index 초과 시 초기화
            if self.currentTime >= self.animationTime:
                self.currentTime = 0
                if self.blind == True:
                    self.image = self.images[0]
                else:
                    self.image = self.images[rd.randrange(1, len(self.images))]