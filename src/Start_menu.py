import pygame
import pygame_menu

class Start_menu(pygame_menu.Menu):
    def __init__(self,menu_width,menu_height):
        self.menu = pygame_menu.Menu(title="SmallGame",width=menu_width,height=menu_height,theme=pygame_menu.themes.THEME_BLUE)

    def menuelements(self,functionpass=None):
        self.menu.add.text_input("Name:",default="Pindor").get_value()
        self.menu.add.label("A small rpg game \n inspired by fire emblem",max_char=-1,font_size=24)
        self.menu.add.button("Play",functionpass,"game")
        self.menu.add.button("Quit",pygame_menu.events.EXIT)