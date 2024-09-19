import pygame

class AnimationSprite(pygame.sprite.Sprite):
    def __init__(self, position, images):
        super(AnimationSprite, self).__init__()

        size = (200, 200) #이미지 사이즈

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