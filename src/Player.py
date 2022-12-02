import pygame
import json
class Player(pygame.sprite.Sprite):
  def __init__(self,HP=100,MP=100,ATK=50,DEF=20,SPD=50):
    super().__init__()
    self.HP = HP
    self.MP = MP
    self.atk = ATK
    self.defense = DEF
    self.image = pygame.image.load("assets/Player/Player.png")
    self.rect = self.image.get_rect()
    self.speed = SPD
  def up(self):
    self.rect.y += -1*self.speed
  def down(self):
    self.rect.y += self.speed
  def left(self):
    self.rect.x += -1*self.speed
  def right(self):
    self.rect.x += self.speed
