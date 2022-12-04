import pygame
import src.Enemy
class Player(pygame.sprite.Sprite):
  def __init__(self,ATK=1,image="assets/Player/Mlord sprite.png",x=250,y=250):
    super().__init__()
    self.atk = ATK
    self.image = pygame.image.load(image)
    self.image.set_colorkey((255, 174, 201))
    self.image = self.image.convert_alpha(self.image)
    self.rect = self.image.get_rect()
    self.rect.x =x
    self.rect.y =y
    self.speed = self.rect.width
  def up(self):
    self.rect.centery += -1*self.speed
  def down(self):
    self.rect.centery += self.speed
  def left(self):
    self.rect.centerx += -1*self.speed
  def right(self):
    self.rect.centerx += self.speed
  # def attack(self,enemy=src.Enemy.Enemy):
  #   enemy.HP = enemy.HP - self.atk
