'''
This module contains the high scores state class.
'''

from sdl2 import sdlttf
import sdl2.ext

from ..utils.high_score_utils import load_high_scores
from ..service_locator.service_locator import (ServiceLocator, FONT_MANAGER,
                                               GAME_STATE_MANAGER)

from .abstract_game_state import AbstractGameState

FILE_NAME = 'high_scores.txt'

TEXT_COLOR = sdl2.SDL_Color(0, 255, 0)


class HighScoresState(AbstractGameState):
    '''
    This class represents the high scores state.
    '''

    def __init__(self):
        '''
        Initializes the high scores state.
        '''

        self.menu_font = ServiceLocator.get(FONT_MANAGER).fonts['menu']
        self.small_font = ServiceLocator.get(FONT_MANAGER).fonts['small']

        self.no_high_scores_surface = sdlttf.TTF_RenderText_Solid(
            self.menu_font, b'No high scores', TEXT_COLOR)

        self.esc_surface = sdlttf.TTF_RenderText_Solid(
            self.small_font, b'(Press ESC to return to the menu)', TEXT_COLOR)

        self.no_high_scores_texture = None
        self.esc_texture = None

        self.high_scores = load_high_scores()

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
        if event.type == sdl2.SDL_KEYDOWN:
            if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                ServiceLocator.get(GAME_STATE_MANAGER).set_state('menu')
