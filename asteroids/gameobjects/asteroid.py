import random

from sdl2 import SDL_SetRenderDrawColor
from sdl2.sdlgfx import lineColor

from .abstract_game_object import AbstractGameObject
from ..utils.math_utils import rotate_point, get_point_on_circle


class Asteroid(AbstractGameObject):
    '''
    This class represents an asteroid.
    '''

    def __init__(self, x: int, y: int, radius: int, velocity: tuple, angular_velocity: int, rotation: int, color: int):
        self.position = (x, y)
        self.radius = radius
        self.velocity = velocity
        self.angular_velocity = angular_velocity
        self.health = 100
        self.rotation = rotation
        self.color = color or 0xFF00FF00

        self.points = []
        for i in range(0, 5):
            range_start = int(360 / 5 * i)
            range_end = int(360 / 5 * (i + 1))
            angle = random.randint(range_start, range_end)
            point = get_point_on_circle((0, 0), self.radius, angle)
            self.points.append(point)

    def hit(self):
        '''
        This method is called when the asteroid is hit by a bullet.
        '''
        self.health -= 10

    def is_dead(self) -> bool:
        '''
        Returns True if the asteroid is dead, False otherwise.
        '''
        return self.health <= 0

    def render(self, renderer):
        '''
        Renders the asteroid.
        '''
        for i in range(0, 5):
            start_point = self.points[i]
            start_point = rotate_point(
                start_point, self.rotation, (0, 0))
            end_point = self.points[(i + 1) % 5]
            end_point = rotate_point(end_point, self.rotation, (0, 0))
            lineColor(renderer, int(self.position[0] + start_point[0]),
                      int(self.position[1] + start_point[1]),
                      int(self.position[0] + end_point[0]),
                      int(self.position[1] + end_point[1]),
                      self.color)
            SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255)

    def update(self, delta_time):
        '''
        Updates the asteroid.
        '''
        delta_time_seconds = delta_time / 1000
        self.position = (
            self.position[0] + self.velocity[0] * delta_time_seconds,
            self.position[1] + self.velocity[1] * delta_time_seconds
        )
        if self.position[0] < -self.radius:
            self.position = (800 + self.radius, self.position[1])
        elif self.position[0] > 800 + self.radius:
            self.position = (-self.radius, self.position[1])

        if self.position[1] < -self.radius:
            self.position = (self.position[0], 600 + self.radius)
        elif self.position[1] > 600 + self.radius:
            self.position = (self.position[0], -self.radius)

        self.rotation += self.angular_velocity * delta_time_seconds

    def handle_events(self, event):
        '''
        Not used.
        '''