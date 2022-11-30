import pygame

class Button(pygame.sprite.Sprite):

    def __init__(self,
                 width=150,
                 height=150,
                 color=(0, 0, 0),
                 xpos=0,
                 ypos=0,
                 text="None",
                 textpos=(0,0)):
        super().__init__()
        self.width,self.height = width,height
        self.color = color
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = xpos, ypos
        text_color = (255 - color[0],255 - color[1], 255 - color[2])
        self.textpos = textpos
        self.text = pygame.font.SysFont(None,24).render(text, True, text_color)
        self.image.blit(self.text, textpos)
