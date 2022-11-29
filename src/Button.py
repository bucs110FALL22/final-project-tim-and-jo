import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self,width=150,height=150,color=[0,0,0],xpos=0,ypos=0):
        super().__init__(self)
        self.width = width
        self.height = height
        self.color = color
        self.x, self.y = xpos, ypos
      