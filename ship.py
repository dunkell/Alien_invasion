import os

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """飞船类"""

    def __init__(self, ai_game):
        """初始化飞船"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 获取当前文件路径
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, 'images', 'ship.bmp')

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # 将飞船放置在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
