import pygame
import json
class Player(pygame.sprite.Sprite):
  def __init__(self,HP=100,MP=100,ATK=50,DEF=20,SPD=10,image="assets/Player/Mlord sprite.png",x=0,y=0):
    super().__init__()
    self.HP = HP
    self.MP = MP
    self.atk = ATK
    self.defense = DEF
    self.image = pygame.image.load(image)
    # self.move_left=False
    # self.move_right=False
    # self.move_up=False
    # self.move_down=False
#    self.image.convert_alpha()
#    self.image.set_colorkey([0,0,0])
    self.rect = self.image.get_rect()
    self.rect.x =x
    self.rect.y =y
    self.speed = SPD
  def up(self):
    self.rect.centery += -1*self.speed
  def down(self):
    self.rect.centery += self.speed
  def left(self):
    self.rect.centerx += -1*self.speed
  def right(self):
    self.rect.centerx += self.speed
  def update():
    pass