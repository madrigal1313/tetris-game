import pygame
import enum
import os

class pieceShape(enum.Enum):
  LONG = 'long.png'
  T = 't.png'
  SQUARE = 'square.png'
  Z_LEFT = 'left_z.png'
  Z_RIGHT = 'right_z.png'
  L_LEFT = 'left_l.png'
  L_RIGHT = 'right_l.png'

class Piece(pygame.sprite.Sprite):
  def __init__(self, shape: pieceShape, startX = None) -> None:
    pygame.sprite.Sprite.__init__(self)
    
    self.shape = shape
    self.image = pygame.transform(
    pygame.image.load(os.path.join(shape.value)), 30, 30)
    self.mask = pygame.mask.from_surface(self.image)
    self.rect = self.image.get_rect()
    self.rect[0] = 30
    self.rect[1] = 30

  def rotate(self) -> None:
    pass

def create_new_piece():
  pass

class testpiece(pygame.sprite.Sprite):
  def __init__(self, picture, width, height, rotation, x = 250, y = 0):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(pygame.image.load(os.path.join(picture)), (width, height))
    self.image = pygame.transform.rotate(self.image, rotation)
    self.rect = self.image.get_rect()
    self.x = x
    self.y = y
    self.rect = self.rect.move(x, y)

testgroup = pygame.sprite.Group()

def drawGrid():
  if gridLinesEnabled:
    for i in range(1, 21):
      pygame.draw.line(screen, (0, 0, 0), (gridPos[0][0], i*30), (gridPos[1][0], i*30)) #hor
    for i in range(1, 11):
      pygame.draw.line(screen, (0, 0, 0), (i*30, gridPos[0][1]), (i*30, gridPos[1][1])) #ver
  else:
    pygame.draw.line(screen, (0, 0, 0), (gridPos[0][0], gridPos[0][1]), (gridPos[1][0], gridPos[0][1]))
    pygame.draw.line(screen, (0, 0, 0), (gridPos[1][0], gridPos[1][1]), (gridPos[0][0], gridPos[1][1]))
    pygame.draw.line(screen, (0, 0, 0), (gridPos[0][0], gridPos[0][1]), (gridPos[0][0], gridPos[1][1]))
    #pygame.draw.line(screen, (0, 0, 0), (gridPos[1][0], gridPos[1][1]), (gridPos[1][0], gridPos[0][1]))
  
  
  pygame.draw.line(screen, (0, 0, 0), (300, gridPos[0][1]), (500, gridPos[0][1]))
  pygame.draw.line(screen, (0, 0, 0), (300, gridPos[1][1]), (300, gridPos[0][1]))
  pygame.draw.line(screen, (0, 0, 0), (300, gridPos[1][1]), (500, gridPos[1][1]))
    

gridPos = [(30, 30), (300, 600)]
gridLinesEnabled = False
interval = 60 # how many pixels per tetris square

pygame.init()
screen = pygame.display.set_mode([500, 630])
screenRect = screen.get_rect()
clock = pygame.time.Clock()

new_piece = False

#x = 275
#y = 0
r = 0
addX = 0
addY = 0





while True:
  drawGrid()
  if new_piece:
    rightZ = testpiece('right_z.png', 90, 60, -90 * r, 210 + addX, 0 + addY)
    square = testpiece('square.png', 60, 60, 0, 30, 530)
    activeShape = rightZ
  else:
    rightL = testpiece('right_l.png', 90, 60, -90 * r, 210 + addX, 0 + addY)
    square = testpiece('square.png', 60, 60, 0, 30, 530)
    rightZ = testpiece('right_z.png', 90, 60, 0, 350, 90)
    activeShape = rightL



  
  i = 1
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      break

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        print("right")
        if (activeShape.x + 30) <= 600:
          addX += 30
        else:
          while (activeShape.x + i) <= 600:
            addX += 1
            i += 1
            print("heheha")
        print(activeShape.x)
      elif event.key == pygame.K_LEFT:
        print("left")
        if (activeShape.x - 30) >= 0:
          addX -= 30
          print("yay")
        else:
          while (activeShape.x - i) >= 0:
            addX -= 1
            i += 1
        print(activeShape.x)
      elif event.key == pygame.K_UP:
        print("up")
        r += 1
  
  activeShape.rect.clamp_ip(screenRect)
  testgroup.add(rightL, rightZ, square, rightZ)
  testgroup.draw(screen)
  if activeShape.rect.colliderect(square):
    addX = 0
    addY = 0
    activeShape.rect.union_ip(square.rect)
    new_piece = True
    x = rightL.x
    y = rightL.y
    rot = r
    rightL = testpiece('right_l.png', 90, 60, rot, x, y)
    r = 0
  else:  
    addY += 5
  testgroup.empty()

  pygame.display.update()
  screen.fill((255, 255, 255))

pygame.quit()