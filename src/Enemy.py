import pygame
import random
"""
Monster and Boss classes were scrapped for this Enemy class (combined both)
"""

class Enemy(pygame.sprite.Sprite):
  def __init__(self,hp = 5, speed=10,type_enemy="Cyclope",x = 0,y = 0):
    super().__init__()
    self.HP = hp
    self.image = pygame.image.load(f"assets/Enemy/{type_enemy}.png")
    self.speed = speed
    self.rect = self.image.get_rect()
    self.type = type_enemy
    self.rect.x =x
    self.rect.y =y
  def movement(self, player):
    """
    Moves the enemy
    """
    self.rect_x += self.speed + random.randrange(-10,10)
    self.rect_y += self.speed + random.randrange(-10,10)
  def death(self):
    self.image = pygame.image.load("assets/Enemy/dead.png")
    self.rect_x = 10000
    self.rect_y = 10000
    pass