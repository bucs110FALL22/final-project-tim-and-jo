import pygame

class Background(pygame.sprite.Sprite):
  def __init__(self,primary_image=None):
    """
    Initializes the background class and gives it attributes
    """
    super().__init__()
    self.background = pygame.image.load(primary_image)
    self.backgroundconvert = pygame.image.load(primary_image)
    self.rect = self.background.get_rect()

  # def replacebackground(self,new_primary_image=None):
    # """
    # Intended to replace the background should the need arise
    # """  
    # self.background = pygame.image.load(new_primary_image)

 # def resizebackground(self, primary_image=None):
    # pygame.sprite.Sprite.__init__(self):
    #     self.image = pygame.image.load("testImage.png").convert()
    #     self.image.set_colorkey((255,255,255))
    #     # return a width and height of an image
    #     self.size = self.image.get_size()
    #     # create a 2x bigger image than self.image
    #     self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0]*2), int(self.size[1]*2)))
    #     # draw bigger image to screen at x=100 y=100 position
    #     self.screen.blit(self.bigger_img, [100,100])