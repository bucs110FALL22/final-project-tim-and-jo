import pygame
import random
"""
Monster and Boss classes were scrapped for this Enemy class (combined both)
"""

class Enemy(pygame.sprite.Sprite):
  def __init__(self, base_level=5, buff=0,hp = 10, atk=10, defense=10, speed=3,type_enemy="slime",x = 0,y = 0):
    super().____init__(self)
    self.base_LVL = base_level
    self.HP = hp * self.base_LVL + self.buff_LVL
    self.buff_LVL = buff
    self.atk = atk * self.base_LVL + self.buff_LVL
    self.defense = defense * self.base_LVL + self.buff_LVL
    self.image = pygame.image.load(f"assets/{type_enemy}.png").convert_alpha()
    self.speed = speed
    self.rect = self.image.get_rect()
    self.type = type_enemy
    self.position = (x,y)
  def movement(self, player):
    """
    Moves the enemy
    """
    self.rect_x += self.speed + player.pos_x
    self.rect_y += self.speed + player.pos_y
  def death(self):
    pass