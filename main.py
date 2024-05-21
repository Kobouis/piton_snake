import pygame
import random


# ! Размер клетки 30 на 30 пикселей

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = pygame.transform.scale(picture, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Snake:
    def __init__(self, tiles, x_speed, y_speed, keys):
        self.keys = keys
        self.tiles = tiles
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self): # Перемещение всех тайлов змеи
        for i in range(len(self.tiles)-1, 0, -1):
            self.tiles[i].rect.x = self.tiles[i-1].rect.x
            self.tiles[i].rect.y = self.tiles[i-1].rect.y
        self.tiles[0].rect.move_ip(self.x_speed, self.y_speed)

    def draw(self):
        for i in self.tiles:
            i.draw()

    def key_handler(self, event): # Управление
        if event in self.keys:
            self.x_speed, self.y_speed = self.keys[event]

    def add_tile(self):
        self.tiles.append(GameSprite(snake_hull, w, h, 0, 30))


# Размеры экрана 600 на 600
width = 600
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Python snake')
clock = pygame.time.Clock()

w = 30
h = 30

# Змея

snake_hull = pygame.image.load("snake_hull.png")
snake = Snake([GameSprite(snake_hull, w, h, 0, 30)], 30, 0,
              {
    pygame.K_a: [-30, 0],
    pygame.K_d: [30, 0],
    pygame.K_w: [0, -30],
    pygame.K_s: [0, 30]
})

# Яблоки
foodx = round(random.randrange(0, height - 30) / 30.0) * 30.0
foody = round(random.randrange(0, width - 30) / 30.0) * 30.0

apple_sprite = pygame.image.load("apple.png")
apple_list = [GameSprite(apple_sprite, w, h, foodx, foody)]

run = True
while run:
    window.fill((255,0,230))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            snake.key_handler(i.key)

    snake.update()
    snake.draw()

    for i in apple_list:
        i.draw()
        if snake.tiles[0].rect.colliderect(i.rect):
            snake.add_tile()
            apple_list.remove(i)
            foodx = round(random.randrange(0, height - 30) / 30.0) * 30.0
            foody = round(random.randrange(0, width - 30) / 30.0) * 30.0
            apple_list.append(GameSprite(apple_sprite, w, h, foodx, foody))

    pygame.display.update()
    clock.tick(5)

pygame.display.quit()