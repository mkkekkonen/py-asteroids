'''
This file contains utility functions for math operations.
'''

import math


def get_point_on_circle(center, radius, angle):
    '''
    This function returns a point on a circle given the center, radius, and angle.
    '''
    x = center[0] + radius * math.cos(math.radians(angle))
    y = center[1] + radius * math.sin(math.radians(angle))
    return (int(x), int(y))


def rotate_point(point, angle, origin=(0, 0)):
    '''
    Rotates a point around an origin by a given angle.

    :param point: The point to rotate (x, y).
    :param angle: The angle to rotate in degrees.
    :param origin: The origin to rotate around (default is (0, 0)).
    :return: The rotated point (x', y').
    '''

    angle_rad = math.radians(angle)

    ox, oy = origin
    px, py = point

    # Translate point back to origin
    translated_px = px - ox
    translated_py = py - oy

    # Rotate point
    qx = (translated_px * math.cos(angle_rad) -
          translated_py * math.sin(angle_rad))
    qy = (translated_px * math.sin(angle_rad) +
          translated_py * math.cos(angle_rad))

    # Translate point back
    qx += ox
    qy += oy

    return int(qx), int(qy)


def is_point_on_right_side_of_line(start_point: tuple, end_point: tuple, point: tuple):
    '''
    This function returns True if the point is on the right side of the line, False otherwise.
    '''
    return ((end_point[0] - start_point[0]) * (point[1] - start_point[1])
            - (end_point[1] - start_point[1]) * (point[0] - start_point[0]) > 0)


def calculate_intersection_points(line_start, line_end, window_width, window_height):
    """
    Calculate the intersection points of a line with the window borders.

    :param line_start: The start point of the line (x, y).
    :param line_end: The end point of the line (x, y).
    :param window_width: The width of the window.
    :param window_height: The height of the window.
    :return: A list of intersection points (x, y).
    """
    intersections = []

    def line_intersection(p1, p2, q1, q2):
        """
        Calculate the intersection point of two lines (p1-p2 and q1-q2).

        :param p1: The start point of the first line (x, y).
        :param p2: The end point of the first line (x, y).
        :param q1: The start point of the second line (x, y).
        :param q2: The end point of the second line (x, y).
        :return: The intersection point (x, y) or None if no intersection.
        """
        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        xdiff = (p1[0] - p2[0], q1[0] - q2[0])
        ydiff = (p1[1] - p2[1], q1[1] - q2[1])

        div = det(xdiff, ydiff)
        if div == 0:
            return None  # Lines do not intersect

        d = (det(p1, p2), det(q1, q2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return x, y

    # Define the window borders as lines
    borders = [
        ((0, 0), (window_width, 0)),  # Top border
        ((0, 0), (0, window_height)),  # Left border
        ((window_width, 0), (window_width, window_height)),  # Right border
        ((0, window_height), (window_width, window_height))  # Bottom border
    ]

    for border in borders:
        intersection = line_intersection(
            line_start, line_end, border[0], border[1])
        if intersection:
            x, y = intersection
            if 0 <= x <= window_width and 0 <= y <= window_height:
                intersections.append((int(x), int(y)))

    return intersections
