class Settings:
    """设置类"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.screen_width_default = 1200
        self.screen_height_default = 800

        # 飞船移动速度
        self.ship_speed = 0.5

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_hight = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
