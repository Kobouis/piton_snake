from pygame import *

#! Размер клетки 30 на 30 пикселей

class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Snake(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        if self.rect.x >= 0 and self.rect.x <= 600:
            self.rect.x += self.x_speed
        elif self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 600:
            self.rect.x = 570
        
        if self.rect.y >= 0 and self.rect.y <= 600:
            self.rect.y += self.y_speed
        elif self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > 600:
            self.rect.y = 570
                
# Размеры экрана 600 на 600
width = 600
height = 600

window = display.set_mode((width, height))
display.set_caption('Python snake')
clock = time.Clock()

# Змея
w = 30
h = 30
snake_speed_x = 30
snake_speed_y = 0
snake_head = Snake("snake_right.png", w,h,30,30,0,0)

#Яблоки

play = True
while play:

    window.fill((255,0,230))

    for e in event.get():
        if e.type == QUIT:
            play = False
        
        elif e.type == KEYDOWN:
            if e.key == K_w:
                snake_speed_y = -30
                snake_speed_x = 0

            if e.key == K_a:
                snake_speed_y = 0
                snake_speed_x = -30

            if e.key == K_s:
                snake_speed_y = 30
                snake_speed_x = 0

            if e.key == K_d:
                snake_speed_y = 0
                snake_speed_x = 30
    
    snake_head.x_speed = snake_speed_x
    snake_head.y_speed = snake_speed_y

    snake_head.draw()
    snake_head.update()

    display.update()
    clock.tick(5)

