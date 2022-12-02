# The controller
# Extremely basic for now - flush out later
# I now understand why programmers have many monitors in many orientations
import pygame
import json
import src.Button
import pygame_menu
import src.Player
class Controller:
  def __init__(self):
    """
    Initializes pygame and the game
    args: self
    return: none
    """
    pygame.init()
    self.player = src.Player.Player()
    self.screen = pygame.display.set_mode()
    self.width, self.height = pygame.display.get_window_size()
    self.fillbackground = pygame.Surface(pygame.display.get_window_size())
    self.fillbackground.fill((255,255,255))
    self.state = "menu"
    self.menu = pygame_menu.Menu(title="HELP MEEEEE",width=self.width,height=self.height,theme=pygame_menu.themes.THEME_BLUE)
    self.menu.add.label("Play Me",max_char=-1,font_size=14)
    self.menu.add.button("Play",self.change_state,"game")
    self.menu.add.button("Quit",pygame_menu.events.EXIT)
    # ministate is intended to only be used in gameplay/ in the game loop
    # to call certain functions that only make sense within gameplay
    # self.ministate = "none"

  def change_state(self,state):
    self.state = state
    return self.state

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

  def gameloop(self):
    """
    Loop that controls gameplay
    args: self
    return: none
    """

    self.screen.blit(self.fillbackground,(0,0))

    self.player.rect.x = 256
    self.player.rect.y = 256
    self.screen.blit(self.player.image,self.player.rect)
    events = pygame.event.get()
    for event in events:
      if event == pygame.K_p:
        self.change_state("menu")
      elif event == pygame.K_w:
        self.player.up()
      pygame.display.flip() 


  def menuloop(self):
    """
    Loop that controls the start screen/menu
    args: self
    return: None
    """
    events = pygame.event.get()
    if self.menu.is_enabled():
      self.menu.update(events)
      self.menu.draw(self.screen)
    
    pygame.display.update()

      


  # def pauseloop(self):
  #   """
  #   Method to pause the game - should only be called if none of the other game actions are running
  #   and the user calls it
  #   args: self
  #   return: new state or return to game state
  #   """
  #   print("Pauseloop")
  #   self.state = input("Change state to:")
  #   self.ministate = "none"

  # def fight(berligerent1,berligerent2):
  #   """
  #   Method to make things fight each other
  #   args: berligerent1, berligerent2
  #   return: stat changes of berligerents (change object attributes)
  #   """
  #   berligerent2.hp = berligerent2.hp - berligerent1.atk
  #   berligerent1.hp = berligerent1.hp - berligerent2.atk
  #   if berligerent2.hp == 0:
  #     defeatedone = berligerent2.type
  #     # replace with proper way to display enemy deaths later
  #     print(f"{defeatedone} was slain")
  #     berligerent2.death()
  # def interact(self,entity1,entity2):
  #   """
  #   Intent - this goes first, then calls the fight method if those interacting are enemies
  #   args: entity1, entity2
  #   return: MiniMenu Object with selection options to call other controller functions (e.g. the fight() function)
  #   """
  #   if entity1.group == "rock" or entity2.group == "rock":
  #     print("Not Interactable")
  #   if entity1.group == entity2.group:
  #     # insert proper minimenu object here
  #     self.ministate = "interactscreen"


