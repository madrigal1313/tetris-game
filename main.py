import pygame
import enum
import os
from typing import Union

gridPos = [(0, 0), (300, 700)] # (0, 3), (300,  700)
interval = 60 # how many pixels per tetris square

pygame.init()
screen = pygame.display.set_mode([600, 700])
screenRect = screen.get_rect()
clock = pygame.time.Clock()

class pieceShape(enum.Enum):
  LONG = 'long.png'
  T = 't.png'
  SQUARE = 'square.png'
  Z_LEFT = 'left_z.png'
  Z_RIGHT = 'right_z.png'
  L_LEFT = 'left_l.png'
  L_RIGHT = 'right_l.png'

class Piece:
  def __init__(self, shape: pieceShape) -> None:
    self.x = 0
    self.y = 0
    self.shape = shape
    self.rotation = 0 #range from 0 to 3 and defines rotation state

  # def rotate()

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

#x = 275
#y = 0
r = 0
addX = 0
addY = 0

def drawGrid():
  for i in range(25): pygame.draw.line(screen, (0, 0, 0), (gridPos[0][0], i*28), (gridPos[1][0], i*28), width = 1) #hor
  for i in range(1, 11): pygame.draw.line(screen, (0, 0, 0), (i*30, gridPos[0][1]), (i*30, gridPos[1][1]), width = 1) #ver

newPiece = False

while True:
  # clock.tick(5)
  drawGrid()
  
  rightL = testpiece('right_l.png', 90, 60, -90 * r, 210 + addX, 0 + addY)
  square = testpiece('square.png', 60, 60, 0, 30, 530)
  i = 1
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      break

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        print("right")
        if (rightL.x + 30) <= 600:
          addX += 30
        else:
          while (rightL.x + i) <= 600:
            addX += 1
            i += 1
            print("heheha")
        print(rightL.x)
      elif event.key == pygame.K_LEFT:
        print("left")
        if (rightL.x - 30) >= 0:
          addX -= 30
          print("yay")
        else:
          while (rightL.x - i) >= 0:
            addX -= 1
            i += 1
        print(rightL.x)
      elif event.key == pygame.K_DOWN:
        print("down")
      elif event.key == pygame.K_UP:
        print("up")
        r += 1
  
  rightL.rect.clamp_ip(screenRect)
  testgroup.add(rightL, square)
  #for drawing in pygame.sprite.Group.sprites(testgroup):
    #print(drawing)
    #screen.blit(drawing.image, (drawing.x, drawing.y))
  testgroup.draw(screen)
  if rightL.rect.colliderect(square):
    rightL.rect.union_ip(square.rect)
    newPiece = True
  else:  
    addY += 5
  testgroup.empty()

  pygame.display.update()
  screen.fill((255, 255, 255))
pygame.quit()