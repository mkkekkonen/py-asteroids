import random

from ..gameobjects import Asteroid


class AsteroidGenerator():
    '''
    This class is used to generate asteroids.
    '''

    def generate(self, num_asteroids):
        '''
        Generates a list of asteroids.
        '''

        asteroids = []
        for _ in range(num_asteroids):
            x = random.randint(0, 800)
            y = random.randint(0, 600)
            radius = random.randint(10, 30)
            velocity = (random.randint(-100, 100), random.randint(-100, 100))
            angular_velocity = random.randint(10, 50)
            rotation = 0
            color = 0xFF00FF00
            asteroid = Asteroid(
                x, y, radius, velocity, angular_velocity, rotation, color
            )
            asteroids.append(asteroid)
        return asteroids
