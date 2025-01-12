'''
This module contains the high scores state class.
'''

from sdl2 import sdlttf
import sdl2.ext

from ..utils.high_score_utils import load_high_scores
from ..utils.math_utils import format_time
from ..service_locator.service_locator import (ServiceLocator, FONT_MANAGER,
                                               GAME_STATE_MANAGER)
from ..gfx import MenuLines

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

        self.high_score_surfaces = []

        self.no_high_scores_texture = None
        self.esc_texture = None

        self.high_scores = []

        self.menu_lines = MenuLines()

    def reset(self):
        self.high_scores = load_high_scores()
        self.high_score_surfaces = []

        for _, high_score in enumerate(self.high_scores):
            name = high_score['name']
            time = high_score['time']
            formatted_time = format_time(time)

            high_score_text = f'{name} - {formatted_time}'

            high_score_surface = sdlttf.TTF_RenderText_Solid(
                self.menu_font, high_score_text.encode('utf-8'), TEXT_COLOR)

            self.high_score_surfaces.append(high_score_surface)

    def render(self, renderer):
        no_high_scores = len(self.high_scores) == 0

        if no_high_scores and self.no_high_scores_texture is None:
            self.no_high_scores_texture = sdl2.ext.renderer.Texture(
                renderer,
                self.no_high_scores_surface)

        if self.esc_texture is None:
            self.esc_texture = sdl2.ext.renderer.Texture(
                renderer,
                self.esc_surface)

        renderer.clear()

        self.menu_lines.render(renderer)

        if no_high_scores:
            renderer.copy(self.no_high_scores_texture, dstrect=(100, 100))

        else:
            y = 100
            for high_score_surface in self.high_score_surfaces:
                high_score_texture = sdl2.ext.renderer.Texture(
                    renderer,
                    high_score_surface)

                renderer.copy(high_score_texture, dstrect=(100, y))

                y += 50

        renderer.copy(self.esc_texture, dstrect=(100, 450))

        renderer.present()

    def update(self, delta_time: float):
        self.menu_lines.update(delta_time)

    def handle_events(self, event):
        if event.type == sdl2.SDL_KEYDOWN:
            if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                ServiceLocator.get(GAME_STATE_MANAGER).set_state('menu')
