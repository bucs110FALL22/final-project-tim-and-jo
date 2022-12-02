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
import src.Enemy

class Controller:
  def __init__(self):
    """
    Initializes pygame and the game
    args: self
    return: none
    """
    pygame.init()
    self.screen = pygame.display.set_mode()
    self.width, self.height = self.screen.get_size()
    self.player = src.Player.Player()
    self.enemy = src.Enemy.Enemy(type_enemy="Cyclope sprite",x=self.width/2 + random.randrange(10,50),y=self.height/3 + random.randrange(10, 50))
    self.bigger_enemy = src.Enemy.Enemy(type_enemy="DLord sprite",x=self.width/2,y=self.height/15)
    self.background = src.Background.Background("assets/Tiles/fe8map6.png")

    self.fillbackground = pygame.Surface(pygame.display.get_window_size())
    self.fillbackground.fill((255,255,255))
    self.state = "menu"
    self.menu = pygame_menu.Menu(title="HELP MEEEEE",width=self.width,height=self.height,theme=pygame_menu.themes.THEME_BLUE)
    self.menu.add.text_input("Name:",default='Pindor')
    self.menu.add.label("A extremely small attempt at a fire emblem style game",max_char=-1,font_size=24)
    self.menu.add.button("Play",self.change_state,"game")
    self.menu.add.button("Quit",pygame_menu.events.EXIT)
    # ministate is intended to only be used in gameplay/ in the game loop
    # to call certain functions that only make sense within gameplay
    # self.ministate = "none"

  def player_convert_alpha(self):
    self.player.image.set_colorkey([255, 174, 201])
    self.player.image.convert_alpha()
    
  def enemy_convert_alpha(self):
    self.enemy.image.set_colorkey([255, 174, 201])
    self.enemy.image.convert_alpha()
    self.bigger_enemy.image.set_colorkey([255, 174, 201])
    self.bigger_enemy.image.convert_alpha()
  
  def change_state(self,state):
    self.state = state
    return self.state

  def scaleimage(self):
  #  self.scale = self.backgroundconvert.get()
  #  self.backgroundconvert = pygame.transform.scale(int(self.scale([0]))*2, int(self.scale([1]))*2)
    # self.background.background = pygame.transform.chop(self.fillbackground,self.background.rect)

    self.image = pygame.image.load("assets/Tiles/fe8map6.png")
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
    self.player_convert_alpha()
    self.enemy_convert_alpha()
    self.scaleimage()
    self.screen.blit(self.image, self.background.rect)
    self.screen.blit(self.player.image,self.player.rect)
    self.screen.blit(self.enemy.image,self.enemy.rect)
    self.screen.blit(self.bigger_enemy.image,self.bigger_enemy.rect)
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
          self.change_state("menu")
        elif event.key == pygame.K_LEFT:
          self.player.left()
        elif event.key == pygame.K_RIGHT:
          self.player.right()
        elif event.key == pygame.K_UP:
          self.player.up()
        elif event.key == pygame.K_DOWN:
          self.player.down()    
    self.screen.blit(self.player.image,self.player.rect)
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

  
  def fight(self):
        self.enemy.hp = self.enemy.hp - self.player.atk
        self.player.rect.x = self.player.rect.x + random.randrange(-20, 20)
        self.player.rect.y = self.player.rect.y + random.randrange(-20,20)
        if self.enemy.hp <=0:
          self.enemy.death()

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


