'''
This module contains the Ship class, which represents the player's ship.
'''

import math

import sdl2
from sdl2 import SDL_SetRenderDrawColor
from sdl2.sdlgfx import trigonColor

from .abstract_game_object import AbstractGameObject
from ..utils.math_utils import get_point_on_circle
from ..game.bullet_manager import BulletManager
from ..mixer import Mixer


BULLET_VELOCITY = 100


class Ship(AbstractGameObject):
    '''
    This class represents the player's ship.
    '''

    def __init__(self, position: int, radius: int,
                 velocity: float, acceleration: float, rotation: int):
        self.position = position
        self.circle_radius = radius
        self.velocity = velocity
        self.acceleration = acceleration
        self.rotation = rotation
        self.color = 0xFF00FF00

    def render(self, renderer):
        '''
        Renders the ship as a triangle inside a circle.
        '''
        top_point = get_point_on_circle(
            self.position, self.circle_radius, self.rotation + 270)
        left_point = get_point_on_circle(
            self.position, self.circle_radius, self.rotation + 135)
        right_point = get_point_on_circle(
            self.position, self.circle_radius, self.rotation + 45)

        trigonColor(renderer, top_point[0], top_point[1], left_point[0],
                    left_point[1], right_point[0], right_point[1], self.color)
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255)

    def update(self, delta_time: float):
        pass

    def handle_events(self, event: sdl2.SDL_Event):
        if event.type == sdl2.SDL_KEYDOWN:
            if event.key.keysym.sym == sdl2.SDLK_RIGHT:
                self.rotation += 5
            elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                self.rotation -= 5
            elif event.key.keysym.sym == sdl2.SDLK_UP:
                self.acceleration = 0.1
            elif event.key.keysym.sym == sdl2.SDLK_DOWN:
                self.acceleration = -0.1
            elif event.key.keysym.sym == sdl2.SDLK_SPACE:
                (BulletManager.get_instance()
                    .create_bullet(
                        self.position,
                        self.get_bullet_velocity(),
                        self.rotation,
                        0xFF00FF00))
                Mixer.get_instance().play_sound('laser')

    def get_bullet_velocity(self):
        '''
        Returns the velocity of a newly created bullet.
        '''

        bullet_rotation_rad = math.radians(self.rotation - 90)

        return (BULLET_VELOCITY * math.cos(bullet_rotation_rad),
                BULLET_VELOCITY * math.sin(bullet_rotation_rad))
