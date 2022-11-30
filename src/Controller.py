# The controller
# Extremely basic for now - flush out later
# I now understand why programmers have many monitors in many orientations
import pygame
import json
class Controller:
  def __init__(self):
    """
    Initializes pygame and the game
    args: self
    return: none
    """
    pygame.init()
    self.screen = pygame.display.set_mode()
    self.state = "menu"
    # ministate is intended to only be used in gameplay/ in the game loop
    # to call certain functions that only make sense within gameplay
    self.ministate = "none"

  def mainloop(self):
    """
    Big loop that controls all other subloops
    args: self
    return: None
    """
    print("I Lived")
    while True:
      if self.state == "menu":
        self.menuloop()
      elif self.state == "game":
        self.gameloop()
      elif self.state == "quit":
        exit()

  def gameloop(self):
    """
    Loop that controls gameplay
    args: self
    return: none
    """
    print("In Game Loop")
    self.state = input("Change Loop To:")

  def menuloop(self):
    """
    Loop that controls the start screen/menu
    args: self
    return: None
    """
    print("In Menu Loop")
    self.state = input("Change Loop To:")


  def pauseloop(self):
    """
    Method to pause the game - should only be called if none of the other game actions are running
    and the user calls it
    args: self
    return: new state or return to game state
    """
    print("Pauseloop")
    self.state = input("Change state to:")
    self.ministate = "none"

  def fight(berligerent1,berligerent2):
    """
    Method to make things fight each other
    args: berligerent1, berligerent2
    return: stat changes of berligerents (change object attributes)
    """
    berligerent2.hp = berligerent2.hp - berligerent1.atk
    berligerent1.hp = berligerent1.hp - berligerent2.atk
    if berligerent2.hp == 0:
      defeatedone = berligerent2.type
      # replace with proper way to display enemy deaths later
      print(f"{defeatedone} was slain")
      berligerent2.death()
  def interact(self,entity1,entity2):
    """
    Intent - this goes first, then calls the fight method if those interacting are enemies
    args: entity1, entity2
    return: MiniMenu Object with selection options to call other controller functions (e.g. the fight() function)
    """
    if entity1.group == "rock" or entity2.group == "rock":
      print("Not Interactable")
    if entity1.group == entity2.group:
      # insert proper minimenu object here
      self.ministate = "interactscreen"


