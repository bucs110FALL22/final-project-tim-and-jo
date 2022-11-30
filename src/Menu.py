import src.Button
import pygame

class Menu(pygame.sprite.Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        self.playbutton = src.Button.Button(100,100,[255,255,255],720,720)
