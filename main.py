import pygame
import time
import enum
import os
from typing import Union

sizeScreen = 800
pygame.init()
screen = pygame.display.set_mode([sizeScreen, sizeScreen])
interval = sizeScreen / 10 # how many pixles per tetris square

class pieceShape(enum.Enum):
  LONG = 0
  T = 1
  SQUARE = 2
  Z_LEFT = 3
  Z_RIGHT = 4
  L_LEFT = 5
  L_RIGHT = 6

  @classmethod
  def returnDrawShape(cls, shape) -> list:
    pieceDrawMapPos = {
      cls.SQUARE: [
        (0, 0),
        (20, 0),
        (0, 20),
        (20, 20)
      ],
      cls.LONG: [
        ()
      ]
    }
    return pieceDrawMapPos[shape]


class PartialPiece(pygame.sprite.Sprite):
  def __init__(self, attachedPieceGroup: pygame.sprite.Group, pos: Union[tuple, list], color: Union[tuple, list]) -> None:
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface(list(pos))
    self.image.fill(list(color))
    self.rect = self.image.get_rect()

class Piece:
  def __init__(self, shape: pieceShape) -> None:
    self._group = pygame.sprite.Group()
    self.shape = shape
    if shape == pieceShape.SQUARE:
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

#x = 275
#y = 0
r = 0
addX = 0
addY = 0



while True:
  rightL = testpiece('right_l.png', 140, 100, -90 * r, 400 + addX, 0 + addY)
  square = testpiece('square.png', 90, 90, 0, 275, 300)
  i = 1
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      break
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        print("right")
        if (rightL.x + 50) <= 500:
          addX += 50
        else:
          while (rightL.x + i) <= 500:
            addX += 1
            i += 1
            print("heheha")
        print(rightL.x)
      elif event.key == pygame.K_LEFT:
        print("left")
        if (rightL.x - 50) >= 0:
          addX -= 50
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
  rightL.rect.clamp_ip(screen.get_rect())
  testgroup.add(rightL, square)
  #for drawing in pygame.sprite.Group.sprites(testgroup):
    #print(drawing)
    #screen.blit(drawing.image, (drawing.x, drawing.y))
  screen.fill((255, 255, 255)) # make backround white
  testgroup.draw(screen)
  if not rightL.rect.colliderect(square):
    addY += 5
  testgroup.empty()
  pygame.display.update() # update screen
  #screen.fill((255, 255, 255)) # make backround white
pygame.quit()