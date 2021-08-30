import pygame

class Variables:
  def __init__(self):
    self.WIN_SIZE = (500, 500)
    self.CAPTION = "Beyond Home"
    self.clock = pygame.time.Clock()
    self.BLACK = (0, 0, 0)
    self.WHITE = (255, 255, 255)
    self.x = 0
    self.y = 0
    self.PLAYER_WIDTH = 25
    self.PLAYER_HEIGHT = 50
    self.player = pygame.Rect(0, 0, self.PLAYER_WIDTH, self.PLAYER_HEIGHT)
    self.VEL = 2

def game():
  global win, vars

  pygame.init()

  win = pygame.display.set_mode(vars.WIN_SIZE)
  pygame.display.set_caption(vars.CAPTION)

  game_loop()

def game_loop():
  global win, vars

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        break

    handle_movement()

    render()

    vars.clock.tick(30)

def render():
  global win, vars

  win.fill(vars.WHITE)

  pygame.draw.rect(win, vars.BLACK, vars.player)

  pygame.display.update()

def handle_movement():
  global win, vars

  pressed = pygame.key.get_pressed()

  if pressed[pygame.K_UP] or pressed[pygame.K_w]:
    if vars.VEL < vars.y:
      vars.y -= vars.VEL
  if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
    if 500 - vars.PLAYER_HEIGHT - vars.VEL > vars.y:
      vars.y += vars.VEL
  if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
    if vars.VEL < vars.x:
      vars.x -= vars.VEL
  if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
    if 500 - vars.PLAYER_WIDTH - vars.VEL > vars.x:
      vars.x += vars.VEL
  
  vars.player = pygame.Rect(vars.x, vars.y, vars.PLAYER_WIDTH, vars.PLAYER_HEIGHT)

vars = Variables()

game()