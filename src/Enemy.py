import pygame
"""
Monster and Boss classes were scrapped for this Enemy class (combined both)
"""

class Enemy(pygame.sprite.Sprite):
  def __init__(self,hp = 5, speed=10,type_enemy="Cyclope",x = 0,y = 0, *groups):
    super().__init__(*groups)
    self.HP = hp
    self.image = pygame.image.load(f"assets/Enemy/{type_enemy}.png")
    self.image.set_colorkey((255, 174, 201))
    self.image.convert_alpha(self.image)
    self.speed = speed
    self.rect = self.image.get_rect()
    self.type = type_enemy
    self.rect.x =x
    self.rect.y =y
#  def movement(self):
#    """
#    Moves the enemy
#    self.rect_x += self.speed + random.randrange(-10,10)
#    self.rect_y += self.speed + random.randrange(-10,10)
  def death(self):
    """
    Janky way to ensure that the enemy is dead and will not interact with the player
    """
    self.image = pygame.image.load("assets/Enemy/dead.png")
    self.image.set_colorkey((255, 174, 201))
    self.image.convert_alpha(self.image)
    self.rect_x = 10000
    self.rect_y = 10000
    self.rect.width =0
    self.rect.height = 0
    pass