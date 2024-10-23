from pygame import *
import random
from time import time as timer
init()
mixer.init()

win_width = 700
win_heidth = 500

font1 = font.SysFont("Arial", 35)
lose1 = font1.render("Игрок 1 проиграл!", True, (180, 0, 0))
lose2 = font1.render("Игрок 2 проиграл!", True, (180, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.player_width = player_width
        self.player_height = player_height
        self.image = transform.scale(image.load(player_image), (self.player_width, self.player_height))
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
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height, speed_x, speed_y):
        super().__init__(player_image, player_x, player_y, player_speed, player_width, player_height)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y -= self.speed_y
        if self.rect.y > win_heidth - self.player_height or self.rect.y < 0:
            self.speed_y *= -1
        if sprite.collide_rect(player1, self) or sprite.collide_rect(player2, self):
            self.speed_x *= -1

window = display.set_mode((win_width, win_heidth))
display.set_caption("Пинг понг")

clock = time.Clock()
FPS = 60

game = True
finish = False

player1 = Player("racket.png", 620, 250, 5, 65, 125)
player2 = Player("racket.png", 15, 250, 5, 65, 125)
ball = Ball("ball.png", 350, 250, 0, 40, 40, 5, 4)
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
        ball.update()
        if ball.rect.x < -50:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > 750:
            finish = True
            window.blit(lose2, (200, 200))
        

    display.update()
    clock.tick(FPS)
