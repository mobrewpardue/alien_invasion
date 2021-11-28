import sys
import pygame

from settings import Settings

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    
    # Represents the entire surface of the game.
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Saving Félicette")

    #Start the main loop for the game.
    while True:
    
        #Watch for the keyboard & mouse events.
        for event in pygame.event.get():
            #Redraw the screen during each pass through the loop.
            screen.fill(ai_settings.bg_color)
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            if event.type==pygame.QUIT:
                sys.exit()


run_game()