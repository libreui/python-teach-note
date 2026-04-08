import pygame


class Audio:
    def __init__(self, tw):
        self.tw = tw
        self.res = tw.res

    def start(self):
        audio = pygame.mixer.Sound(self.res.audio_start)
        audio.play()
