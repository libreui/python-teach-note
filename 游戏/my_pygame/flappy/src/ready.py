from resource import ResourceManager


class Ready:
    def __init__(self, flappy):
        self.flappy = flappy
        self.screen = self.flappy.screen
        self.screen_rect = self.screen.get_rect()
        self.resource = ResourceManager()
        self.image = self.resource.get_other_images()['message']
        self.rect = self.image.get_rect(center=self.screen_rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class GameOver:
    def __init__(self, flappy):
        self.flappy = flappy
        self.screen = self.flappy.screen
        self.screen_rect = self.screen.get_rect()
        self.resource = ResourceManager()
        self.image = self.resource.get_other_images()['gameover']
        self.rect = self.image.get_rect(center=self.screen_rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
