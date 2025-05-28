import pygame
from pygame.locals import * # * is a library including QUIT, KEY_DOWN, KEY_UP, MOUSEBUTTON(UP/DOWN), etc 
pygame.init() # initialize modules like font renderer, timer, window/screen, etc

WIDTH, HEIGHT = 590, 590
ground_scroll=-100 # location of the ground after scrolled
scroll_speed=2
window=pygame.display.set_mode((WIDTH, HEIGHT))
background_img=pygame.image.load("Skyline Jump\orangesky.jpg")
ground_img=pygame.image.load("Skyline Jump\soil.png")

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

play = True
while play:
    window.blit(background_img, (0,0))
    window.blit(ground_img, (ground_scroll, 400))
    ground_scroll-=scroll_speed

    if ground_scroll<-150:
        ground_scroll=-100
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            play = False
    pygame.display.update()
pygame.quit()
