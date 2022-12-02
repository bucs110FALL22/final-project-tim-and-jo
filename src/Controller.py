# The controller
# Extremely basic for now - flush out later
# I now understand why programmers have many monitors in many orientations
import pygame
import json
import src.Button
import pygame_menu
import src.Player
import random
import src.Background

class Controller:
  def __init__(self):
    """
    Initializes pygame and the game
    args: self
    return: none
    """
    pygame.init()
    self.player = src.Player.Player()
    self.background = src.Background.Background("assets/Tiles/Map 1 sprite.png","assets/Tiles/Map 1 sprite.png","assets/Tiles/Map 1 sprite.png")
    self.screen = pygame.display.set_mode()
    self.width, self.height = self.screen.get_size()
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

  def scaleimage(self):
  #  self.scale = self.backgroundconvert.get()
  #  self.backgroundconvert = pygame.transform.scale(int(self.scale([0]))*2, int(self.scale([1]))*2)
    # self.background.background = pygame.transform.chop(self.fillbackground,self.background.rect)

    self.image = pygame.image.load("assets/Tiles/Map 1 sprite.png")
    self.image = pygame.transform.scale(self.image, (self.width, self.height))

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
    Loop that sets up and controls gameplay
    args: self
    return: none
    """
    
    self.screen.blit(self.fillbackground,(0,0))
    onlyonetime = 0
    while onlyonetime ==0:
      self.scaleimage()
      self.player.rect.x = self.width/2
      self.player.rect.y = self.height/2
      self.screen.blit(self.image, self.background.rect)
      self.screen.blit(self.player.image,self.player.rect)
      onlyonetime +=1
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
          self.change_state("menu")
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          self.player.move_left = True
        if event.key == pygame.K_RIGHT:
          self.player.move_right = True
        if event.key == pygame.K_UP:
          self.player.move_up = True
        if event.key == pygame.K_DOWN:
          self.player.move_down = True
#      elif event.type == pygame.KEYUP:
#        if event.key == pygame.K_LEFT:
#          self.player.move_left = False
#        if event.key == pygame.K_RIGHT:
#          self.player.move_right = False
#        if event.key == pygame.K_UP:
#          self.player.move_up = False
#        if event.key == pygame.K_DOWN:
#          self.player.move_down = False
    if(self.player.move_left):
      self.player.left()
      self.screen.blit(self.player.image,(self.player.rect.x, self.player.rect.y))
    if(self.player.move_right):
      self.player.right()
      self.screen.blit(self.player.image,(self.player.rect.x, self.player.rect.x))
    if(self.player.move_up):
      self.player.up()
      self.screen.blit(self.player.image,(self.player.rect.x, self.player.rect.y))
    if(self.player.move_down):
      self.player.down()
      self.screen.blit(self.player.image,(self.player.rect.x, self.player.rect.y))
    pygame.display.update()


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

  
  # def fight(self):
  #   while encounter == True:
  #     if pygame.sprite.groupcollide(Player, Enemy) == True:
  #       enemy.hp = enemy.hp - player.atk
  #       if enemy.hp >=0:
  #         enemy.kill()
  #       if player.hp >= 0:
  #         player.kill()
  #       else: 
  #         atk_roll = randrange(3)
  #         if atk_roll == 0:
  #           player.hp = player.hp - enemy.atk
  #         if atk_roll == 1:
  #           player.hp = player.hp - (enemy.atk * 1.5)
  #         if atk_roll == 2:
  #           player.hp = player.hp - (enemy.atk * 2)


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


