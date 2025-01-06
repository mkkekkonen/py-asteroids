'''
This module contains the Particle class.
'''

import random

import sdl2
from sdl2.sdlgfx import lineColor

from ..utils.math_utils import rotate_point

from .abstract_game_object import AbstractGameObject


class Particle(AbstractGameObject):
    '''
    This class represents a particle.
    '''

    def __init__(self, position: tuple, radius: int, velocity: tuple,
                 angular_velocity: float, color: int, lifetime: int):
        self.position = position
        self.radius = radius
        self.velocity = velocity
        self.angular_velocity = angular_velocity
        self.color = color
        self.lifetime = lifetime
        self.elapsed_time = 0
        self.dead = False
        self.rotation = 0

        x, y = self.position

        self.points = []
        for i in range(0, 3):
            angle_range_start = int(360 / 3 * i)
            angle_range_end = int(360 / 3 * (i + 1))
            angle = random.randint(angle_range_start, angle_range_end)
            initial_point = (x, y - self.radius)
            point = rotate_point(initial_point, angle, position)
            self.points.append(point)

        self.start_time = sdl2.SDL_GetTicks()

    def render(self, renderer):
        for i, start_point in enumerate(self.points):
            end_point = self.points[(i + 1) % 3]
            start_point = rotate_point(
                start_point, self.rotation, self.position)
            end_point = rotate_point(end_point, self.rotation, self.position)
            lineColor(
                renderer, start_point[0], start_point[1], end_point[0], end_point[1], self.color)

    def update(self, delta_time):
        self.elapsed_time = sdl2.SDL_GetTicks() - self.start_time
        self.dead = self.elapsed_time > self.lifetime

        delta_seconds = delta_time / 1000

        self.position = (self.position[0] + self.velocity[0] * delta_seconds,
                         self.position[1] + self.velocity[1] * delta_seconds)
        self.rotation += self.angular_velocity * delta_seconds
        self.rotation %= 360

    def handle_events(self, event):
        '''
        No-op.
        '''
