# The controller
# Extremely basic for now - flush out later
import pygame
import json

class Controller:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode()
    self.state = "menu"

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
  
  def gameloop(self):
    pass

  def menuloop(self):
    pass

  def mainloop(self):
    while True:
      if self.state == "menu":
        self.menuloop()
      if self.state == "game":
        self.gameloop()

