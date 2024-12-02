'''
This module contains the Game class, which is the main class of the game.
'''

import sdl2.ext

from ..gameobjects import Ship
from .asteroid_generator import AsteroidGenerator
from .singleton_container import SingletonContainer


class Game():
    '''
    This class represents the game root instance.
    '''

    def __init__(self, window):
        self.renderer = sdl2.ext.Renderer(
            window, flags=sdl2.SDL_RENDERER_SOFTWARE)
        self.ship = Ship((400, 300), 20, 0, 0, 0, 0x00FF00)
        self.asteroids = AsteroidGenerator().generate(5)

    def render(self):
        '''
        Renders the game and game objects.
        '''

        self.renderer.clear()

        self.ship.render(self.renderer.renderer)

        for asteroid in self.asteroids:
            asteroid.render(self.renderer.renderer)

        SingletonContainer.get_instance().get_singleton(
            'BulletManager').render(self.renderer.renderer)

        self.renderer.present()

    def update(self, delta_time: float):
        '''
        Updates the game and game objects.
        '''
        self.asteroids = [
            asteroid for asteroid in self.asteroids if not asteroid.is_dead()]
        for asteroid in self.asteroids:
            asteroid.update(delta_time)

        SingletonContainer.get_instance().get_singleton(
            'BulletManager').update(delta_time)

    def handle_events(self, event):
        '''
        Handles events for the game and game objects.
        '''
        self.ship.handle_events(event)
