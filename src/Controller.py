# The controller
# Extremely basic for now - flush out later
# I now understand why programmers have many monitors in many orientations
import pygame
import json
import pygame_menu
import src.Player
import random
import src.Background
import src.Enemy
import time

class Controller:

  def __init__(self):
    """
    Initializes pygame and the game - quite long due to need to initialize many objects
    args: self
    return: none
    """
    pygame.init()
    self.screen = pygame.display.set_mode()
    self.width, self.height = self.screen.get_size()
    self.player = src.Player.Player()
    self.enemy = src.Enemy.Enemy(type_enemy="Cyclope sprite",x=self.width / 2 + random.randrange(10, 50), y=self.height / 3 + random.randrange(10, 50))
    self.bigger_enemy = src.Enemy.Enemy(type_enemy="DLord sprite",x=self.width / 2,y=self.height / 15,hp=15)
    self.background = src.Background.Background("assets/Tiles/fe8map6.png")
    self.state = "menu"
    self.menu = pygame_menu.Menu(title="SmallGame",width=self.width,height=self.height, theme=pygame_menu.themes.THEME_BLUE)
    self.menu.add.label("A small rpg game \n inspired by fire emblem",max_char=-1, font_size=24)
    self.menu.add.text_input(title="Name:", default="Pindor").get_value()
    self.menu.add.button("Play", self.change_state, "game")
    self.menu.add.button("Quit", pygame_menu.events.EXIT)
    self.player_group = pygame.sprite.Group([self.player])
    self.enemy_group = pygame.sprite.Group([self.enemy, self.bigger_enemy])
    self.all_sprites = pygame.sprite.Group()
    self.all_sprites.add(self.player_group, self.enemy_group)

  def player_name_save(self, name):
    """
    saves the name of the player to a json file
    args: self, name
    return: None
    """
    print(name)
    file = open("assets/Player/RecordofPersons.json")
    hof = json.load(file)
    print(hof)
    file = open("assets/Player/RecordofPersons.json", "w")
    date = time.strftime("%m/%d/%Y")
    hof.update({name: f"{name} vanquished the great demon on {date}"})
    print(hof)
    json.dump(hof, file)
    file.close()

  def change_state(self, state):
    """
    Changes the state of the game
    args: self,state
    return: None
    """
    self.state = state
    return self.state

  def drawloop(self):
    self.background.getscaledimage(self.background.background, self.width,self.height)
    self.screen.blit(self.background.background, self.background.rect)
    self.screen.blit(self.enemy.image, self.enemy.rect)
    self.screen.blit(self.bigger_enemy.image, self.bigger_enemy.rect)
    self.screen.blit(self.player.image, self.player.rect)

  def mainloop(self):
    """
    Big loop that controls all other subloops
    args: self
    return: None
    """
    while True:
      if self.state == "menu":
        self.menuloop()
      elif self.state == "game":
        self.gameloop()
      elif self.state == "winstate":
        self.winloop()

  def gameloop(self):
    """
    Loop that sets up and controls gameplay - large due to needing to render game elements
    args: self
    return: none
    """
    events = pygame.event.get()
    collide = pygame.sprite.groupcollide(self.player_group, self.enemy_group,False, False)
    print(collide)
    for _ in collide:
      self.fight()
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
    self.drawloop()
    pygame.display.update()

  def menuloop(self):
    """
    Loop that controls the start screen/menu
    args: self
    return: None
    """
    namedict = self.menu.get_input_data()
    name = namedict.popitem()
    name = str(name)
    self.name = name[24:(len(name) - 2)]
    events = pygame.event.get()
    if self.menu.is_enabled():
      self.menu.update(events)
      self.menu.draw(self.screen)
    pygame.display.update()

  def fight(self):
    """
    function that lets the player and enemies fight
    args: self
    return: none
    """
    self.enemy.HP = self.enemy.HP - self.player.atk
    self.player.rect.x = self.player.rect.x + random.randrange(-50, 50)
    self.player.rect.y = self.player.rect.y + random.randrange(-50, 50)
    if self.enemy.HP <= 0:
      self.enemy.death()
      self.bigger_enemy.HP = self.bigger_enemy.HP - self.player.atk
      self.player.rect.x = self.player.rect.x + random.randrange(-50, 50)
      self.player.rect.y = self.player.rect.y + random.randrange(-50, 50)
    if self.bigger_enemy.HP <= 0:
      self.bigger_enemy.death()
      self.state = "winstate"

  def winloop(self):
    """
    Loop that takes control away from the player to play a cutscene
    args: self
    return: none
    """
    dialougefile = open("assets/Enemy/Boss_dialouge.json")
    file = json.loads(dialougefile.read())
    x = 1
    for i in file["Boss Dialouge"]:
      print(i)
      font = pygame.font.SysFont(None, 24)
      msg = i
      img = font.render(msg, True, (255, 255, 255))
      self.screen.blit(img, ((self.width / 2), (self.height / 2) + (20 * x)))
      x += 1
      pygame.display.update()
      pygame.time.wait(2500)
    dialougefile.close()
    self.player_name_save(self.name)
    exit()
