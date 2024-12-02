'''
This module contains the Bullet class.
'''

import sdl2
from sdl2.sdlgfx import lineColor

from ..utils.math_utils import rotate_point
from .abstract_game_object import AbstractGameObject

BULLET_LENGTH = 5


class Bullet(AbstractGameObject):
    '''
    This class represents a bullet.
    '''

    def __init__(self, position: tuple, velocity: tuple, rotation: int, color: int):
        self.position = position
        self.velocity = velocity
        self.rotation = rotation
        self.color = color
        self.dead = False

    def is_dead(self) -> bool:
        '''
        Returns True if the bullet is dead, False otherwise.
        '''
        return (self.dead
                or self.position[0] < 0
                or self.position[0] > 800
                or self.position[1] < 0
                or self.position[1] > 600)

    def render(self, renderer):
        '''
        Renders the bullet.
        '''
        start_point = (0, int(-BULLET_LENGTH / 2))
        end_point = (0, int(BULLET_LENGTH / 2))
        start_point = rotate_point(start_point, self.rotation)
        end_point = rotate_point(end_point, self.rotation)
        lineColor(renderer, int(self.position[0] + start_point[0]),
                  int(self.position[1] + start_point[1]),
                  int(self.position[0] + end_point[0]),
                  int(self.position[1] + end_point[1]),
                  self.color)
        sdl2.SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255)

    def update(self, delta_time):
        '''
        Updates the bullet's position.
        '''

        delta_seconds = delta_time / 1000

        self.position = (self.position[0] + self.velocity[0] * delta_seconds,
                         self.position[1] + self.velocity[1] * delta_seconds)

    def handle_events(self, event):
        '''
        Not used.
        '''

    def destroy(self):
        '''
        Destroys the bullet.
        '''
        self.dead = True
