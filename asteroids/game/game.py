'''
This module contains the Game class, which is the main class of the game.
'''

import sdl2.ext

from ..gameobjects import Ship


class Game():
    '''
    This class represents the game root instance.
    '''

    def __init__(self, window):
        self.renderer = sdl2.ext.Renderer(
            window, flags=sdl2.SDL_RENDERER_SOFTWARE)
        self.ship = Ship((400, 300), 20, 0, 0, 0, 0x00FF00)

    def render(self):
        '''
        Renders the game and game objects.
        '''

        self.renderer.clear()
        self.ship.render(self.renderer.renderer)
        self.renderer.present()

    def update(self):
        '''
        Updates the game and game objects.
        '''

    def handle_events(self, event):
        '''
        Handles events for the game and game objects.
        '''
        self.ship.handle_events(event)
