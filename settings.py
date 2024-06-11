class Settings:
    """设置类"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.screen_width_default = 1200
        self.screen_height_default = 800

        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 2

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.alien_points = 50

        # 子弹设置
        self.bullet_speed = 3.0
        self.bullet_width = 300
        self.bullet_hight = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # 游戏节奏加快设置
        self.speedup_scale = 1.1
        self.score_scale = 1.5


        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)