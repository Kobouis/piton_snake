from pygame import *
import math

# Размеры экрана

width = 700
height = 500
dimensions = (width, height)

window = display.set_mode((width, height))
background = (125, 188, 240)
display.set_caption('Лабиринт')

#! Классы
class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
        
    def update(self):
        if self.rect.x <= width-80 and self.x_speed > 0 or self.rect.x >= 0 and self.x_speed < 0:
            self.rect.x += self.x_speed
            platforms_touched = sprite.spritecollide(self, walls, False)
            if self.x_speed > 0:
                for p in platforms_touched:
                    self.rect.right = min(self.rect.right, p.rect.left) 
            elif self.x_speed < 0:
                for p in platforms_touched:
                    self.rect.left = max(self.rect.left, p.rect.right)
            
        if self.rect.y <= height-80 and self.y_speed > 0 or self.rect.y >= 0 and self.y_speed < 0:
            self.rect.y += self.y_speed
            platforms_touched = sprite.spritecollide(self, walls, False)
            if self.y_speed > 0:
                for p in platforms_touched:
                    self.rect.bottom = min(self.rect.bottom, p.rect.top)
            elif self.y_speed < 0:
                for p in platforms_touched:
                    self.rect.top = max(self.rect.top, p.rect.bottom)
    def fire(self):
        bullet = Bullet('bullet.png', 20, 15, self.rect.right, self.rect.centery, 50)
        bullets.add(bullet)
        
class Enemy(GameSprite):
    def __init__(self, picture, w, h, x, y, speed):
            GameSprite.__init__(self,  picture, w, h, x, y)
            self.speed = speed
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= width - 80:
            self.direction = 'left'
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Bullet(GameSprite):
    def __init__(self, picture, w, h, x, y, speed):
        GameSprite.__init__(self,  picture, w, h, x, y)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > width+10:
            self.kill()

# Объекты
# Стены
wall_1 = GameSprite('platform_h.png', 300, 50, int(width / 2 - width / 3), int(width / 2))
wall_2 = GameSprite('platform_v.png', 50, 400, 370, 100)
# Пуля

# Спрайты
monster = Enemy('enemy.png', 80, 80, width - 80, 190, 5)

player = Player('hero.png', 80, 80, 5, 420, 0, 0)

final = GameSprite('thumb.jpg', width - 80, 180, 80, 80)
final_sprite = GameSprite('pac-1.png', 80, 80, width - 85, height - 100)

bullets = sprite.Group()
walls = sprite.Group()
monsters = sprite.Group()

monsters.add(monster)
monsters.add(final_sprite)
walls.add(wall_1)
walls.add(wall_2)

# Основной цикл
finish = False
run = True
while run:
    time.delay(50)
    window.fill(background)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                 player.y_speed = -10
            if e.key == K_a:
                 player.x_speed = -10
            if e.key == K_s:
                 player.y_speed = 10
            if e.key == K_d:
                 player.x_speed = 10
            if e.key == K_SPACE:
                player.fire()
        elif e.type == KEYUP:
            if e.key == K_w:
                 player.y_speed = 0
            if e.key == K_a:
                 player.x_speed = 0
            if e.key == K_s:
                 player.y_speed = 0
            if e.key == K_d:
                 player.x_speed = 0

    if not finish:
        window.fill(background)
        walls.draw(window)
        monsters.draw(window)
        monsters.update()
        final_sprite.draw()
        player.draw()
        player.update()
        bullets.update()
        bullets.draw(window)

    sprite.groupcollide(bullets, walls, True, False)
    sprite.groupcollide(bullets, monsters, True, True)

    
    if sprite.collide_rect(player, final_sprite):
       finish = True
       img = image.load('thumb.jpg')
       window.fill((255, 255, 255))
       window.blit(transform.scale(img, (width, height)), (0, 0))

    if sprite.collide_rect(player, monster):
        finish = True
        img = image.load('game-over_1.png')
        d = img.get_width() // img.get_height()
        window.fill((255, 255, 255))
        window.blit(transform.scale(img, (height * d, height)), (90, 0))

    display.update()
