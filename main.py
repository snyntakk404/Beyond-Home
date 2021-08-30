import pygame

class Variables:
  def __init__(self):
    self.WIN_SIZE = (500, 500)
    self.CAPTION = "Beyond Home"
    self.clock = pygame.time.Clock()
    self.BLACK = (0, 0, 0)
    self.WHITE = (255, 255, 255)
    self.PLAYER = pygame.Rect(0, 0, 25, 50)

def game():
  global win, vars

  pygame.init()

  win = pygame.display.set_mode(vars.WIN_SIZE)
  pygame.display.set_caption(vars.CAPTION)

  game_loop()

def game_loop():
  global win, vars

  while True:
    render()

    vars.clock.tick(30)

def render():
  global win, vars

  win.fill(vars.WHITE)

  pygame.draw.rect(win, vars.BLACK, vars.PLAYER)

  pygame.display.update()

vars = Variables()
game()