import pygame as pg
pg.init()


back = '#9A98B5'
clock = pg.time.Clock()
fps = 40
window_size = (500, 500)
run = True

window = pg.display.set_mode(window_size)

class TextArea():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = pg.Rect(x, y, width, height)
      self.fill_color = color
      #возможные надписи
      self.titles = list()



  #добавить текст в список возможных надписей
  def add_text(self, text):
    self.titles.append(text)


  #установить текст
  def set_text(self, number=0, fsize=30, text_color=BLACK):
      self.text = self.titles[number]
      self.image = pg.font.Font(None, fsize).render(self.text, True, text_color)
    
  #отрисовка прямоугольника с текстом
  def draw(self, shift_x=0, shift_y=0):
      pg.draw.rect(mw, self.fill_color, self.rect)
      mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))  class TextArea():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = pg.Rect(x, y, width, height)
      self.fill_color = color
      #возможные надписи
      self.titles = list()



  #добавить текст в список возможных надписей
  def add_text(self, text):
    self.titles.append(text)


  #установить текст
  def set_text(self, number=0, fsize=30, text_color=BLACK):
      self.text = self.titles[number]
      self.image = pg.font.Font(None, fsize).render(self.text, True, text_color)
    
  #отрисовка прямоугольника с текстом
  def draw(self, shift_x=0, shift_y=0):
      pg.draw.rect(mw, self.fill_color, self.rect)
      mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))  

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    window.fill(back) 
    pg.display.update()
    clock.tick(fps)

