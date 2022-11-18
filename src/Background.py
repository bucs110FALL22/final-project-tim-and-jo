import pygame

class Background(pygame.sprite.Sprite):
  def __init__(self,primary_image=None,overlay_image = None,animated_image = None):
    """
    Initializes the background class and gives it attributes
    """
    super.__init__(self)
    self.background = pygame.image.load(primary_image).convert_alpha()
    self.overlay = pygame.image.load(overlay_image).convert_alpha()
    self.animated = pygame.image.load(animated_image).convert_alpha()
    self.rect = self.background.get_rect()

  def replacebackground(self,new_primary_image=None,new_overlay_image=None,new_animated_image=None):
    """
    Intended to replace the background should the need arise
    """  
    self.background = pygame.image.load(new_primary_image).convert_alpha()
    self.overlay = pygame.image.load(new_overlay_image).convert_alpha()
    self.animated = pygame.image.load(new_animated_image).convert_alpha()