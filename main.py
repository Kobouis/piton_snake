from pygame import *
import random

font.init()
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
        
        if self.rect.y >= 0 and self.rect.y <= 600:
            self.rect.y += self.y_speed

class Apple(GameSprite):
    def __init__(self, picture, w, h, x, y):
            GameSprite.__init__(self, picture, w, h, x, y)

    def spawn(self,foodx,foody):
        window.blit(self.image, (foodx,foody))

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

snake_tail = Snake("snake_hull.png", w,h,0,30,0,0)
snake_list = []
length = 1

snake_list.append(snake_tail)

#Яблоки
foodx = round(random.randrange(0,height - 30)/ 30.0) * 30.0
foody = round(random.randrange(0,width - 30)/ 30.0) * 30.0

apple = Apple("apple.png", 30,30,0,0)
apple_list = []
apple_list.append(apple)

count = 0

f1 = font.Font(None, 50)
ext1 = f1.render('Game Over', 1, (255, 255, 0))

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

    counter = f1.render('Score: '+str(count), 1,(255, 255, 0))
    window.blit(counter, (0,0))

    for a in snake_list:
        a.draw()
        a.update()
        a.x_speed = snake_speed_x
        a.y_speed = snake_speed_y
        if a.rect.x < 0 or a.rect.x > 600 or a.rect.y < 0 or a.rect.y > 600:
            window.blit(ext1, (220,300))


    for i in apple_list:
        i.spawn(foodx,foody)
        if snake_tail.rect.x == foodx and snake_tail.rect.y == foody:
            apple_list.remove(i)
            length += 1
            count += 1
            foodx = round(random.randrange(0,height - 30)/ 30.0) * 30.0
            foody = round(random.randrange(0,width - 30)/ 30.0) * 30.0
            apple_list.append(apple)

    if len(snake_list) < length:
        snake_list.append(snake_tail)

    display.update()
    clock.tick(5)

