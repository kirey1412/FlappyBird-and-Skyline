import pygame

from pygame.locals import *
pygame.init()

WIDTH, HEIGHT = 800, 900
ground_scroll=0
scroll_speed=2
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
background_img=pygame.image.load("bg.png")
ground_img=pygame.image.load("ground.png")

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for i in range(3):
            img=pygame.image.load(f"bird{i+1}.png")
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x, y]
    def update(self):
        print(self.counter)
        self.counter+=1
        flapdown=5
        if self.counter>flapdown:
            self.counter=0
            self.index+=1
            if self.index>=len(self.images):
                self.index=0
        self.image=self.images[self.index]

birdgroup=pygame.sprite.Group()
bird1=Bird(100, HEIGHT/2)
birdgroup.add(bird1)

        
        
run = True
while run:
    screen.blit(background_img, (0,0))
    birdgroup.draw(screen)
    birdgroup.update()
    screen.blit(ground_img, (ground_scroll, 700))
    ground_scroll-=scroll_speed

    if ground_scroll<-100:
        ground_scroll=0
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            run = False
    pygame.display.update()
pygame.quit()