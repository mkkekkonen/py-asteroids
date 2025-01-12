'''
This module contains the menu state.
'''

import sdl2
from sdl2 import sdlttf
import sdl2.ext

from .abstract_game_state import AbstractGameState
from ..gfx import MenuLines
from ..service_locator.service_locator import (ServiceLocator, FONT_MANAGER,
                                               QUIT_FLAG_CONTAINER, GAME_STATE_MANAGER,
                                               STATS_MANAGER)

SELECTED_COLOR = sdl2.SDL_Color(0, 255, 0)
UNSELECTED_COLOR = sdl2.SDL_Color(0, 70, 0)

START_GAME_TEXT = b'Start Game'
QUIT_GAME_TEXT = b'Quit Game'

START_GAME = 0
QUIT_GAME = 1


class MenuState(AbstractGameState):
    '''
    This class represents the menu state.
    '''

    def __init__(self):
        '''
        Initializes the menu state.
        '''

        self.menu_font = ServiceLocator.get(FONT_MANAGER).fonts['menu']

        self.selected_start_game_surface = sdlttf.TTF_RenderText_Solid(
            self.menu_font, START_GAME_TEXT, SELECTED_COLOR)
        self.selected_quit_game_surface = sdlttf.TTF_RenderText_Solid(
            self.menu_font, QUIT_GAME_TEXT, SELECTED_COLOR)

        self.unselected_start_game_surface = sdlttf.TTF_RenderText_Solid(
            self.menu_font, START_GAME_TEXT, UNSELECTED_COLOR)
        self.unselected_quit_game_surface = sdlttf.TTF_RenderText_Solid(
            self.menu_font, QUIT_GAME_TEXT, UNSELECTED_COLOR)

        self.selected_start_game_texture = None
        self.selected_quit_game_texture = None
        self.unselected_start_game_texture = None
        self.unselected_quit_game_texture = None

        self.selected_item = START_GAME

        self.menu_lines = MenuLines()

    def reset(self):
        '''
        Resets the game state.
        '''

    def render(self, renderer):
        '''
        Renders the game state.
        '''

        start_selected = self.selected_item == START_GAME
        quit_selected = self.selected_item == QUIT_GAME

        if self.selected_start_game_texture is None:
            self.selected_start_game_texture = sdl2.ext.renderer.Texture(
                renderer,
                self.selected_start_game_surface)

        if self.selected_quit_game_texture is None:
            self.selected_quit_game_texture = sdl2.ext.renderer.Texture(
                renderer,
                self.selected_quit_game_surface)

        if self.unselected_start_game_texture is None:
            self.unselected_start_game_texture = sdl2.ext.renderer.Texture(
                renderer,
                self.unselected_start_game_surface)

        if self.unselected_quit_game_texture is None:
            self.unselected_quit_game_texture = sdl2.ext.renderer.Texture(
                renderer,
                self.unselected_quit_game_surface)

        renderer.clear()

        self.menu_lines.render(renderer)

        renderer.copy(
            self.selected_start_game_texture if start_selected
            else self.unselected_start_game_texture,
            dstrect=(100, 100))
        renderer.copy(
            self.selected_quit_game_texture if quit_selected
            else self.unselected_quit_game_texture,
            dstrect=(100, 200))

        renderer.present()

    def update(self, delta_time: float):
        '''
        Updates the game state.
        '''

        self.menu_lines.update(delta_time)

    def handle_events(self, event: sdl2.SDL_Event):
        '''
        Handles events for the game state.
        '''

        if event.type == sdl2.SDL_KEYDOWN:
            if event.key.keysym.sym == sdl2.SDLK_DOWN:
                self.selected_item = QUIT_GAME
            elif event.key.keysym.sym == sdl2.SDLK_UP:
                self.selected_item = START_GAME
            elif event.key.keysym.sym == sdl2.SDLK_RETURN:
                if self.selected_item == START_GAME:
                    ServiceLocator.get(STATS_MANAGER).reset()
                    ServiceLocator.get(GAME_STATE_MANAGER).set_state('game')
                elif self.selected_item == QUIT_GAME:
                    ServiceLocator.get(QUIT_FLAG_CONTAINER).set_quit_flag()
