import sys
import pygame

from bullet import Bullet
from settings import Settings
from ship import Ship
from alien import Alien

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # 是否全屏标识
        self.is_fullscreen = False

    def _create_fleet(self):
        """创建外星人群"""
        alien = Alien(self)

        #  一行外星人个数
        alien_width = alien.rect.width
        alien_space_x = self.settings.screen_width - (2 * alien_width)

        number_aliens_x = alien_space_x / (2 * alien_width)

        # 多少行外星人
        alien_height = alien.rect.height
        alien_space_y = self.screen.get_height() - (3 * alien_height) - self.ship.rect.height

        number_rows = int(alien_space_y / (2 * alien_height))

        # 创建外星人群
        for row_number in range(int(number_rows)):
            for alien_number in range(int(number_aliens_x)):
                self._creat_alien(alien_number,row_number)

    def _creat_alien(self, alien_number,row_number):
        """创建一个外星人并将其放在当前行"""
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def run_game(self):
            while True:
                self._check_events()
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_screen()

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
               self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_p:
            self.is_fullscreen = not self.is_fullscreen
            self._toggle_fullscreen()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入到编组bullets中"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            sys.exit()

    def _update_bullets(self):
        """更新子弹的位置，并删除已消失的子弹"""
        self.bullets.update()
        # 删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_aliens(self):
        """更新外星人群中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update(self.settings.alien_speed,self.settings.fleet_direction)

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整群外星人下移，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _toggle_fullscreen(self):
        """切换全屏"""
        if self.is_fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.settings.screen_width = self.settings.screen_width_default
            self.settings.screen_height = self.settings.screen_height_default
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()