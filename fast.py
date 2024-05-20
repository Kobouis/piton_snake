import pygame
import time
pygame.init()
back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


class Label(Area):
    def set_text(self, text, fsize = 12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('Comic Sans MS', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

RED = (255, 0, 0)
GREEN = (0,255, 51)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 10, 100)
cards = []
num_cards = 4
x = 70 

for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 8)
    new_card.set_text('Нажми', 25)
    cards.append(new_card)
    x = x + 100


wait = 0
score = 0
start_time = time.time()
score_goal = 5
time_limit = 10

from random import randint
while True:
    if wait == 0:
        wait = 20
        click = randint(1, num_cards)
        for i in range(num_cards):
            cards[i].color((255, 255, 0))
            if (i + 1) == click:
                cards[i].draw(5, 40)
            else:
                cards[i].fill()
    else:
        wait -= 1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for card in cards:
                if card.collidepoint(*mouse_pos):
                    if card == cards[click - 1]:
                        score += 1
                        card.color(GREEN)
                        card.fill()
                    else:
                        score -= 1
                        card.color(RED)
                        card.fill()
    if score < 0:
        score = 0                   
    current_time = time.time() - start_time
    if current_time >= time_limit:
        result_text = "Время вышло!!!"
        result_color = RED
        break
    if score >= score_goal:
        result_text = "Ты победил!!!"
        result_color = GREEN
        break
    time_label = Label(400, 10, 100, 30, back)
    time_label.set_text("Время: {:.0f}".format(time_limit - current_time), 20, DARK_BLUE)
    time_label.fill()
    time_label.draw()
    score_label = Label(10, 10, 100, 30, back)
    score_label.set_text("Счёт:\n" + str(score), 20, DARK_BLUE)
    score_label.fill()
    score_label.draw()
    pygame.display.update()
    clock.tick(50)

end = Area(0, 0, 600, 600, result_color)
end.fill()

end_text = Label(155, 230, 0, 0, result_color)
end_text.set_text(result_text, 50, (255, 255, 255))
end_text.fill()
end_text.draw()

pygame.display.update()

if result_color == GREEN:
    end_time = time.time()
    total_time = end_time - start_time
    time_label = Label(175, 285, 40, 40, GREEN)
    time_label.set_text('Время прохождения: {:.0f} с.'.format(total_time), 20, DARK_BLUE)
    time_label.fill()
    time_label.draw()
    pygame.display.update()

time.sleep(2) # Пауза для отображения результата
pygame.quit()