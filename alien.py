import os
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_game):
        """初始化外星人及其初始位置"""
        super().__init__()
        self.screen = ai_game.screen

        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "images/alien.bmp")

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

