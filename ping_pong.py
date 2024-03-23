from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, sixe_x, size_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
      # каждый спрайт должен хранить свойство rect - прямоуг., в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

racket1 = Player('pencil.jpg', 30, 200, 4, 50, 10)
racket2 = Player('pencil.jpg', 520, 200, 4, 50, 10)
ball = GameSprite('ball.png', 200, 200, 4,  50, 10)

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill((200, 255, 255))

game = True
finish = False 
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill((200, 255, 255))
        racket1.update_l()
        racket2.update_r()
        racket2.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(60)
