import pygame as pg
from random import randint
pg.init()


back = '#9A98B5'
clock = pg.time.Clock()
fps = 40
window_size = (500, 500)
run = True

window = pg.display.set_mode(window_size)

class Area():
    def __init__(self, x, y, width, height, color):
        self.rect = pg.Rect(x, y, width, height)
        self.fill_color = color

    def set_color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pg.draw.rect(window, self.fill_color, self.rect)
    
    def set_border(self, color, size):
        pg.draw.rect(window, color, self.rect, size)


class Label(Area):
    def set_text(self, fsize, text_color, text):
        self.image = pg.font.SysFont('verdana', fsize).render(text, True, text_color)
    
    def draw(self, shift_x, shift_y):
        self.fill()
        self.set_border('black', 3)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
      
cards = list()

x = 35

for i in range(4):
    card = Label(x, 200, 100, 150, 'yellow')
    card.set_text(20, 'black', 'CLICK')
    #card.set_border('black', 110)
    cards.append(card)
    x += 110

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    window.fill(back) 
    
    for card in cards:
        card.draw(20, 50)

    pg.display.update()
    clock.tick(fps)

