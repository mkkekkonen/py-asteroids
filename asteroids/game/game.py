'''
This module contains the Game class, which is the main class of the game.
'''

import sdl2.ext

from ..gameobjects import Ship
from .asteroid_generator import AsteroidGenerator
from ..mixer import Mixer
from ..game.bullet_manager import BulletManager


class Game():
    '''
    This class represents the game root instance.
    '''

    def __init__(self, window):
        self.renderer = sdl2.ext.Renderer(
            window, flags=sdl2.SDL_RENDERER_SOFTWARE)

        Mixer.get_instance().play_music()

        self.ship = Ship((400, 300), 20, 0, 0, 0)
        self.asteroids = AsteroidGenerator().generate(5)

    def render(self):
        '''
        Renders the game and game objects.
        '''

        self.renderer.clear()

        self.ship.render(self.renderer.renderer)

        for asteroid in self.asteroids:
            asteroid.render(self.renderer.renderer)

        BulletManager.get_instance().render(self.renderer.renderer)

        self.renderer.present()

    def update(self, delta_time: float):
        '''
        Updates the game and game objects.
        '''
        self.asteroids = [
            asteroid for asteroid in self.asteroids if not asteroid.is_dead()]
        for asteroid in self.asteroids:
            asteroid.update(delta_time)

        self.handle_bullet_collisions()

        BulletManager.get_instance().update(delta_time)

    def handle_events(self, event):
        '''
        Handles events for the game and game objects.
        '''
        self.ship.handle_events(event)

    def handle_bullet_collisions(self):
        '''
        Handles collisions between bullets and asteroids.
        '''

        for asteroid in self.asteroids:
            for bullet in BulletManager.get_instance().bullets:
                if asteroid.is_point_inside(bullet.position):
                    print('Hit!')
                    asteroid.hit()
                    bullet.destroy()
