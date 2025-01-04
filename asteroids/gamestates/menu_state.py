'''
This module contains the menu state.
'''

import sdl2
from sdl2 import sdlttf
import sdl2.ext

from .abstract_game_state import AbstractGameState
from ..utils import FontManager


class MenuState(AbstractGameState):
    '''
    This class represents the menu state.
    '''

    def __init__(self):
        '''
        Initializes the menu state.
        '''

        menu_color = sdl2.SDL_Color(0, 255, 0)

        self.menu_font = FontManager.get_instance().fonts['menu']

        self.start_game_surface = sdlttf.TTF_RenderText_Solid(
            self.menu_font, b'Start Game', menu_color)
        self.quit_game_surface = sdlttf.TTF_RenderText_Solid(
            self.menu_font, b'Quit Game', menu_color)

        self.start_game_texture = None
        self.quit_game_texture = None

    def reset(self):
        '''
        Resets the game state.
        '''

    def render(self, renderer):
        '''
        Renders the game state.
        '''

        if self.start_game_texture is None:
            self.start_game_texture = sdl2.ext.renderer.Texture(
                renderer, self.start_game_surface)

        if self.quit_game_texture is None:
            self.quit_game_texture = sdl2.ext.renderer.Texture(
                renderer, self.quit_game_surface)

        renderer.clear()

        renderer.copy(self.start_game_texture, dstrect=(100, 100))
        renderer.copy(self.quit_game_texture, dstrect=(100, 200))

        renderer.present()

    def update(self, delta_time: float):
        '''
        Updates the game state.
        '''

    def handle_events(self, event):
        '''
        Handles events for the game state.
        '''
