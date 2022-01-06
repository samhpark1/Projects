import sys

import pygame
from pygame.sprite import Group

from settings1 import Settings
from game_stats1 import GameStats
from button1 import Button
from ship1 import Ship
from alien1 import Alien
import game_functions1 as gf



def run_game():
    pygame.init();
    ai_settings = Settings();
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height));
    screen = pygame.display.set_mode((900, 600));
    pygame.display.set_caption("Alien Invasion");

    stats = GameStats(ai_settings);
    ship = Ship(ai_settings, screen);
    play_button = Button(ai_settings, screen, "Play");
    bullets = Group();
    aliens = Group();
    alien = Alien(ai_settings, screen);

    gf.create_fleet(ai_settings, screen, ship, aliens);
    
    while True:

        gf.check_events(ai_settings, screen, stats, play_button,
                        ship, aliens, bullets);

        if stats.game_active:
            ship.update();
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets);
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets);

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
                         play_button);

run_game();
