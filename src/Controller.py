# The controller
# Extremely basic for now - flush out later
import pygame

class Controller:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode()


  def fight(berligerent1,berligerent2):
  """
  Method to make things fight each other
  """
    pass

  def interact(entity1,entity2):
  """
  Intent - this goes first, then calls the fight method if those interacting are enemies
  """
    pass