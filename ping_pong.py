from pygame import *
import random
from time import time as timer
init()
mixer.init()

win_width = 700
win_heidth = 500

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_heidth - 130:
            self.rect.y += self.speed
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_heidth - 130:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        ...

window = display.set_mode((win_width, win_heidth))
display.set_caption("Пинг понг")

clock = time.Clock()
FPS = 60

game = True
finish = False

player1 = Player("racket.png", 620, 250, 5, 65, 125)
player2 = Player("racket.png", 15, 250, 5, 65, 125)
ball = Ball("ball.png", 350, 250, 7, 40, 40)
background = transform.scale(image.load("background.jpg"), (win_width, win_heidth))
# mixer.music.load('space.ogg')
# mixer.music.set_volume(0.1)
# mixer.music.play()
# danger = mixer.Sound("Danger.ogg")

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
            
            window.blit(background,(0,0))
            player1.reset()
            player1.update_r()
            player2.reset()
            player2.update_l()
            ball.reset()
            
    display.update()
    clock.tick(FPS)