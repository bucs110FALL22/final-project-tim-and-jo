import pygame
import random
"""
Monster and Boss classes were scrapped for this Enemy class (combined both)
"""


class Enemy(pygame.sprite.Sprite):
  def __init__(self, base=5, buff=1, atk=10, defense=10, speed=3):
    super().____init__(self)
    self.base_LVL = 5
    self.HP = 200 * self.base_LVL or self.buff_LVL
    self.buff_LVL = self.base_LVL + player.LVL
    self.atk = 10 * self.base_LVL or self.buff_LVL
    self.defense = 10 * self.base_LVL or self.buff_LVL
    self.image = pygame.image.load("Goblin / minotaur / boss monster.png").convert_alpha()
    self.speed = 3
    self.rect = self.image.get_rect()
  def movement(self, player):
    """
    Moves the enemy
    """
    self.rect_x += self.speed + player.pos_x
    self.rect_y += self.speed + player.pos_y
  # this should be part of the driver function
  def fight(self):
    """
    Fight function
    """
    encounter = True
    while encounter == True:
      rng = random.randrange(3)
      if rng == 0:
        dmg_dealt = self.atk
      if rng == 1:
        dmg_dealt = self.atk * 1.2
      if rng == 2:
        dmg_dealt = self.atk * 1.5
      if self.hp == 0 or player.hp == 0:
        encounter = False