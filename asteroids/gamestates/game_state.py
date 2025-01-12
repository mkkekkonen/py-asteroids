'''
This module contains the game state class.
'''

import sdl2
import sdl2.ext
from sdl2 import sdlttf

from .abstract_game_state import AbstractGameState

from ..gameobjects.ship import Ship
from ..game.asteroid_generator import AsteroidGenerator
from ..service_locator.service_locator import (ServiceLocator, BULLET_MANAGER,
                                               PARTICLE_MANAGER, FONT_MANAGER,
                                               STATS_MANAGER, GAME_STATE_MANAGER)
from ..utils.math_utils import format_time

FONT_COLOR = sdl2.SDL_Color(0, 255, 0)


class GameState(AbstractGameState):
    '''
    This class represents the game state.
    '''

    def __init__(self):
        self.ship = None
        self.asteroids = None

        self.game_start_time = sdl2.SDL_GetTicks()
        self.elapsed_time = 0

        self.reset()

    def reset(self):
        '''
        Resets the game state.
        '''
        self.ship = Ship((400, 300), 20, 0, 0, 0)
        self.asteroids = AsteroidGenerator().generate(5)

    def render(self, renderer):
        '''
        Renders the game state.
        '''
        renderer.clear()

        ServiceLocator.get(PARTICLE_MANAGER).render(renderer.renderer)

        self.ship.render(renderer.renderer)

        for asteroid in self.asteroids:
            asteroid.render(renderer.renderer)

        ServiceLocator.get(BULLET_MANAGER).render(renderer.renderer)

        self.render_time(renderer)

        renderer.present()

    def update(self, delta_time: float):
        '''
        Updates the game state.
        '''

        self.elapsed_time = sdl2.SDL_GetTicks() - self.game_start_time

        if len(self.asteroids) == 0:
            ServiceLocator.get(GAME_STATE_MANAGER).reset_add_high_score_state()
            ServiceLocator.get(GAME_STATE_MANAGER).set_state('add_high_score')
            return

        self.asteroids = [
            asteroid for asteroid in self.asteroids if not asteroid.is_dead()]
        for asteroid in self.asteroids:
            asteroid.update(delta_time)

        self.handle_bullet_collisions()

        ServiceLocator.get(BULLET_MANAGER).update(delta_time)
        ServiceLocator.get(PARTICLE_MANAGER).update(delta_time)
        ServiceLocator.get(STATS_MANAGER).update(delta_time)

    def handle_events(self, event):
        '''
        Handles events for the game state.
        '''
        self.ship.handle_events(event)

    def handle_bullet_collisions(self):
        '''
        Handles collisions between bullets and asteroids.
        '''
        for asteroid in self.asteroids:
            for bullet in ServiceLocator.get(BULLET_MANAGER).bullets:
                if asteroid.is_point_inside(bullet.position):
                    asteroid.hit()
                    bullet.destroy()

    def render_time(self, renderer):
        '''
        Renders the elapsed time.
        '''

        elapsed_time_text = format_time(self.elapsed_time)

        elapsed_time_surface = sdlttf.TTF_RenderText_Solid(
            ServiceLocator.get(FONT_MANAGER).fonts['game'], elapsed_time_text.encode(), FONT_COLOR)

        elapsed_time_texture = sdl2.ext.renderer.Texture(
            renderer.renderer, elapsed_time_surface)

        renderer.copy(elapsed_time_texture, dstrect=(10, 10))
