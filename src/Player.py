import pygame
import random
class Player(pygame.sprite.Sprite):
  def __init__(self,HP=100,MP=100,ATK=50,DEF=20,SPD=1):
    super().__init__(self)
    self.HP = HP
    self.MP = MP
    self.atk = ATK
    self.defense = DEF
    self.image = pygame.image.load("player.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.speed = SPD
  def up(self):
    self.rect_y -= self.speed
  def down(self):
    self.rect_y += self.speed
  def left(self):
    self.rect_x -= self.speed
  def right(self):
    self.rect_x += self.speed
# part of driver code / controller code
  def interact(self, item):
    return random.randrange(10)
  def fight(self, enemy):
    self.dmg = self.atk - enemy.defense
    self.taken_dmg = enemy.atk - self.defense