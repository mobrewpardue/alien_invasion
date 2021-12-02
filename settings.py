class Settings():
    """A class to store all settings for Saving Félicette."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color =(8,20,30)        
        #ship settings
        self.ship_speed_factor = 1.5