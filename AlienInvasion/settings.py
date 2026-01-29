class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship settings
        # `ship_scale` is a multiplier applied to the original ship image size (1.0 = original size)
        self.ship_scale = 0.17
        # `ship_angle` is the rotation in degrees applied to the ship image (0 = no rotation)
        self.ship_angle = -30

        # Ship settings
        self.ship_speed = 1.5

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
