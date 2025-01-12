'''
This module contains the add high score state.
'''

from sdl2 import sdlttf
import sdl2.ext

from ..service_locator.service_locator import ServiceLocator, FONT_MANAGER, STATS_MANAGER
from ..utils.high_score_utils import load_high_scores
from ..utils.math_utils import format_time

from .abstract_game_state import AbstractGameState

FILE_NAME = 'high_scores.txt'

TEXT_COLOR = sdl2.SDL_Color(0, 255, 0)


class AddHighScoreState(AbstractGameState):
    '''
    This class represents the add high score state.
    '''

    def __init__(self):
        '''
        Initializes the add high score state.
        '''

        self.menu_font = ServiceLocator.get(FONT_MANAGER).fonts['menu']
        self.small_font = ServiceLocator.get(FONT_MANAGER).fonts['small']
        self.high_scores = []

        self.congrats_surface = sdlttf.TTF_RenderText_Solid(
            self.menu_font, b'Congratulations! You made it to the high scores!', TEXT_COLOR)
        if not self.congrats_surface:
            raise RuntimeError(f"Failed to create text surface: {
                               sdl2.sdlttf.TTF_GetError().decode('utf-8')}")

        self.enter_name_surface = sdlttf.TTF_RenderText_Solid(
            self.small_font, b'Enter your name:', TEXT_COLOR)

        self.confirm_surface = sdlttf.TTF_RenderText_Solid(
            self.small_font, b'(Press ENTER to confirm)', TEXT_COLOR)

        self.no_high_score_surface = sdlttf.TTF_RenderText_Solid(
            self.menu_font, b'You did not make it to the high scores.', TEXT_COLOR)

        self.go_to_menu_surface = sdlttf.TTF_RenderText_Solid(
            self.small_font, b'(Press ENTER to go to menu)', TEXT_COLOR)

        self.time_surface = None
        self.name_surface = None

        self.congrats_texture = None
        self.time_texture = None
        self.enter_name_texture = None
        self.name_texture = None
        self.confirm_texture = None
        self.no_high_score_texture = None
        self.go_to_menu_texture = None

        self.name_text = ''
        self.name_changed = False

        self.high_scores = load_high_scores()
        self.made_it = False

    def reset(self):
        if self.check_high_scores():
            self.made_it = True
        else:
            self.made_it = False

    def render(self, renderer):
        if self.made_it:
            self.render_made_it(renderer)
        else:
            self.render_did_not_make_it(renderer)

    def update(self, delta_time: float):
        pass

    def handle_events(self, event):
        if event.type == sdl2.SDL_TEXTINPUT:
            self.name_text += event.text.text.decode('utf-8')
            self.name_changed = True

    def check_high_scores(self):
        '''
        Checks if the player's score is a high score.
        '''
        if len(self.high_scores) < 5:
            return True

        for score in self.high_scores:
            if ServiceLocator.get(STATS_MANAGER).time < score['time']:
                return True

        return False

    def render_made_it(self, renderer):
        '''
        Rendering method to use when the player made it to the high scores.
        '''

        if self.congrats_texture is None:
            self.congrats_texture = sdl2.ext.Texture(
                renderer,
                self.congrats_surface)

        if self.time_texture is None:
            time_text = f'Your time: {format_time(
                ServiceLocator.get(STATS_MANAGER).time)}'
            self.time_surface = sdlttf.TTF_RenderText_Solid(
                self.menu_font, time_text.encode('utf-8'), TEXT_COLOR)
            self.time_texture = sdl2.ext.Texture(
                renderer,
                self.time_surface)

        if self.enter_name_texture is None:
            self.enter_name_texture = sdl2.ext.Texture(
                renderer,
                self.enter_name_surface)

        if self.name_changed is True:
            self.name_surface = sdlttf.TTF_RenderText_Solid(
                self.menu_font, self.name_text.encode('utf-8'), TEXT_COLOR)
            self.name_texture = sdl2.ext.Texture(
                renderer,
                self.name_surface)
            self.name_changed = False

        if self.confirm_texture is None:
            self.confirm_texture = sdl2.ext.Texture(
                renderer,
                self.confirm_surface)

        renderer.clear()

        renderer.copy(self.congrats_texture, dstrect=(100, 100))
        renderer.copy(self.time_texture, dstrect=(100, 150))
        renderer.copy(self.enter_name_texture, dstrect=(100, 250))
        if self.name_texture is not None:
            renderer.copy(self.name_texture, dstrect=(150, 300))
        renderer.copy(self.confirm_texture, dstrect=(100, 370))

        renderer.present()

    def render_did_not_make_it(self, renderer):
        '''
        Rendering method to use when the player did not make it to the high scores.
        '''

        if self.no_high_score_texture is None:
            self.no_high_score_texture = sdl2.ext.Texture(
                renderer,
                self.no_high_score_surface)

        if self.go_to_menu_texture is None:
            self.go_to_menu_texture = sdl2.ext.Texture(
                renderer,
                self.go_to_menu_surface)

        renderer.clear()

        renderer.copy(self.no_high_score_texture, dstrect=(100, 100))
        renderer.copy(self.go_to_menu_texture, dstrect=(100, 200))

        renderer.present()
