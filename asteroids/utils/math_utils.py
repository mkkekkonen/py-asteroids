import math


def get_point_on_circle(center, radius, angle):
    '''
    This function returns a point on a circle given the center, radius, and angle.
    '''
    x = center[0] + radius * math.cos(math.radians(angle))
    y = center[1] + radius * math.sin(math.radians(angle))
    return (int(x), int(y))
