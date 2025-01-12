'''
This module contains the add high score state.
'''

from sdl2 import sdlttf
import sdl2.ext

from asteroids.service_locator.service_locator import (ServiceLocator, FONT_MANAGER,
                                                       STATS_MANAGER, GAME_STATE_MANAGER)
from asteroids.utils.high_score_utils import load_high_scores
from asteroids.utils.math_utils import format_time
from asteroids.gfx import MenuLines

from asteroids.gamestates.abstract_game_state import AbstractGameState

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

        self.menu_lines = MenuLines()

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
        self.menu_lines.update(delta_time)

    def handle_events(self, event):
        if event.type == sdl2.SDL_TEXTINPUT:
            self.name_text += event.text.text.decode('utf-8')
            self.name_changed = True
        elif event.type == sdl2.SDL_KEYDOWN:
            if event.key.keysym.sym == sdl2.SDLK_RETURN:
                if self.made_it:
                    self.add_high_score()
                    ServiceLocator.get(
                        GAME_STATE_MANAGER).reset_high_scores_state()
                    ServiceLocator.get(
                        GAME_STATE_MANAGER).set_state('high_scores')
                else:
                    ServiceLocator.get(
                        GAME_STATE_MANAGER).set_state('menu')

            elif event.key.keysym.sym == sdl2.SDLK_BACKSPACE:
                self.name_text = self.name_text[:-1]
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

    def add_high_score(self):
        '''
        Adds the player's score to the high scores.
        '''
        with open(FILE_NAME, 'w', encoding='utf8') as high_scores_file:
            self.high_scores.append(
                {'name': self.name_text, 'time': ServiceLocator.get(STATS_MANAGER).time})
            self.high_scores = sorted(
                self.high_scores, key=lambda x: x['time'])
            self.high_scores = self.high_scores[:5]
            for score in self.high_scores:
                high_scores_file.write(f'{score["name"]} {score["time"]}\n')

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

        self.menu_lines.render(renderer)

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

        self.menu_lines.render(renderer)

        renderer.copy(self.no_high_score_texture, dstrect=(100, 100))
        renderer.copy(self.go_to_menu_texture, dstrect=(100, 200))

        renderer.present()
