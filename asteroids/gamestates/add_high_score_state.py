'''
This module contains the add high score state.
'''

from sdl2 import sdlttf
import sdl2.ext

import os

from ..utils import FontManager

from .abstract_game_state import AbstractGameState

FILE_NAME = 'high_scores.txt'

TEXT_COLOR = sdl2.SDL_Color(0, 255, 0)


class AddHighScoreState(AbstractGameState):
    '''
    This class represents the add high score state.
    '''

    def __init__(self, game_state_manager):
        '''
        Initializes the add high score state.
        '''

        super().__init__(game_state_manager)

        self.menu_font = FontManager.get_instance().fonts['menu']
        self.small_font = FontManager.get_instance().fonts['small']
        self.high_scores = []

        self.no_high_scores_surface = sdlttf.TTF_RenderText_Solid(
            self.menu_font, b'No high scores', TEXT_COLOR)

        self.esc_surface = sdlttf.TTF_RenderText_Solid(
            self.small_font, b'(Press ESC to return to the menu)', TEXT_COLOR)

        self.no_high_scores_texture = None
        self.esc_texture = None

        self.load_high_scores()

    def load_high_scores(self):
        '''
        Loads the high scores.
        '''

        file_exists = os.path.exists(FILE_NAME)

        if file_exists:
            with open(FILE_NAME, 'r', encoding='utf8') as high_scores_file:
                self.high_scores = high_scores_file.readlines()

    def reset(self):
        pass

    def render(self, renderer):
        if self.no_high_scores_texture is None:
            self.no_high_scores_texture = sdl2.ext.renderer.Texture(
                renderer,
                self.no_high_scores_surface)

        if self.esc_texture is None:
            self.esc_texture = sdl2.ext.renderer.Texture(
                renderer,
                self.esc_surface)

        renderer.clear()

        renderer.copy(self.no_high_scores_texture, dstrect=(100, 100))
        renderer.copy(self.esc_texture, dstrect=(100, 200))

        renderer.present()

    def update(self, delta_time: float):
        pass

    def handle_events(self, event):
        pass
