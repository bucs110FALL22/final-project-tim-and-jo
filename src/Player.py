import pygame
import json
class Player(pygame.sprite.Sprite):
  def __init__(self,ATK=1,SPD=10,image="assets/Player/Mlord sprite.png",x=250,y=250, *groups):
    super().__init__(*groups)
    self.atk = ATK
    self.image = pygame.image.load(image)
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