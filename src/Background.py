import pygame

class Background(pygame.sprite.Sprite):
  """
  Initializes the background class and gives it attributes
  """
  def __init__(self,primary_image=None,overlay_image = None,animated_image = None):
    super.__init__(self)
    self.background = pygame.image.load(primary_image).convert_alpha()
    self.overlay = pygame.image.load(overlay_image).convert_alpha()
    self.animated = pygame.image.load(animated_image).convert_alpha()
    self.rect = self.background.get_rect()