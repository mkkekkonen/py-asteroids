'''
This module contains the add high score state.
'''

from sdl2 import sdlttf
import sdl2.ext

from ..utils import FontManager
from ..utils.high_score_utils import load_high_scores

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

        self.congrats_surface = sdlttf.TTF_RenderText_Solid(
            self.menu_font, b'Congratulations! You made it to the high scores!', TEXT_COLOR)

        self.enter_name_surface = sdlttf.TTF_RenderText_Solid(
            self.small_font, b'Enter your name:', TEXT_COLOR)

        self.confirm_surface = sdlttf.TTF_RenderText_Solid(
            self.small_font, b'(Press ENTER to confirm)', TEXT_COLOR)

        self.name_surface = None

        self.congrats_texture = None
        self.enter_name_texture = None
        self.name_texture = None
        self.confirm_texture = None

        self.name_text = ''
        self.name_changed = False

        self.high_scores = load_high_scores()

    def reset(self):
        pass

    def render(self, renderer):
        if self.congrats_texture is None:
            self.congrats_texture = sdl2.ext.Texture(
                renderer,
                self.congrats_surface)

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
        renderer.copy(self.enter_name_texture, dstrect=(100, 200))
        if self.name_texture is not None:
            renderer.copy(self.name_texture, dstrect=(150, 250))
        renderer.copy(self.confirm_texture, dstrect=(100, 320))

        renderer.present()

    def update(self, delta_time: float):
        pass

    def handle_events(self, event):
        if event.type == sdl2.SDL_TEXTINPUT:
            self.name_text += event.text.text.decode('utf-8')
            self.name_changed = True
