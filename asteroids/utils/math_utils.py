import math


def get_point_on_circle(center, radius, angle):
    '''
    This function returns a point on a circle given the center, radius, and angle.
    '''
    x = center[0] + radius * math.cos(math.radians(angle))
    y = center[1] + radius * math.sin(math.radians(angle))
    return (int(x), int(y))


def rotate_point(point, angle, origin=(0, 0)):
    """
    Rotates a point around an origin by a given angle.

    :param point: The point to rotate (x, y).
    :param angle: The angle to rotate in degrees.
    :param origin: The origin to rotate around (default is (0, 0)).
    :return: The rotated point (x', y').
    """
    angle_rad = math.radians(angle)
    ox, oy = origin
    px, py = point

    qx = int(ox + math.cos(angle_rad) * (px - ox) -
             math.sin(angle_rad) * (py - oy))
    qy = int(oy + math.sin(angle_rad) * (px - ox) +
             math.cos(angle_rad) * (py - oy))
    return qx, qy