'''
This module contains the MenuLines class, which is responsible for rendering
menu background lines.
'''

from sdl2.sdlgfx import lineColor
import sdl2

from asteroids.utils.math_utils import rotate_point, calculate_intersection_points

COLOR = 0xFF008800

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class MenuLines():
    '''
    This class is responsible for rendering the menu background lines.
    '''

    def __init__(self):
        self.intersection_point = (650, 450)
        self.line1_point = (700, 450)
        self.line2_point = rotate_point(
            self.line1_point, 180 / 3, self.intersection_point)
        self.line3_point = rotate_point(
            self.line1_point, 180 / 3 * 2, self.intersection_point)

        self.rotated_line1_point = self.line1_point
        self.rotated_line2_point = self.line2_point
        self.rotated_line3_point = self.line3_point

        self.line1_rotation = 0
        self.line2_rotation = 0
        self.line3_rotation = 0

    def render(self, renderer):
        '''
        Renders the menu background lines.
        '''

        ix, iy = self.intersection_point

        intersections1 = calculate_intersection_points(
            self.intersection_point, self.rotated_line1_point, WINDOW_WIDTH, WINDOW_HEIGHT)
        intersections2 = calculate_intersection_points(
            self.intersection_point, self.rotated_line2_point, WINDOW_WIDTH, WINDOW_HEIGHT)
        intersections3 = calculate_intersection_points(
            self.intersection_point, self.rotated_line3_point, WINDOW_WIDTH, WINDOW_HEIGHT)

        for x, y in intersections1:
            lineColor(renderer.sdlrenderer, ix, iy, x, y, COLOR)
        for x, y in intersections2:
            lineColor(renderer.sdlrenderer, ix, iy, x, y, COLOR)
        for x, y in intersections3:
            lineColor(renderer.sdlrenderer, ix, iy, x, y, COLOR)

        sdl2.SDL_SetRenderDrawColor(renderer.sdlrenderer, 0, 0, 0, 255)

    def update(self, delta_time):
        '''
        Updates the menu background lines.
        '''

        delta_seconds = delta_time / 1000
        rotation_delta = 15 * delta_seconds

        self.line1_rotation += rotation_delta
        self.line2_rotation += rotation_delta * 2
        self.line3_rotation += rotation_delta

        self.rotated_line1_point = rotate_point(
            self.line1_point, self.line1_rotation, self.intersection_point)
        self.rotated_line2_point = rotate_point(
            self.line2_point, self.line2_rotation, self.intersection_point)
        self.rotated_line3_point = rotate_point(
            self.line3_point, self.line3_rotation, self.intersection_point)
