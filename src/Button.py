import pygame


class Button(pygame.sprite.Sprite):

    def __init__(self,
                 width=150,
                 height=150,
                 color=[0, 0, 0],
                 xpos=0,
                 ypos=0,
                 text="None"):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = xpos, ypos
        self.text = pygame.font.SysFont(None,24).render(text, True, [0, 0, 255])
        self.image.blit(self.text, (20, 20))
