'''
A module for managing particles.
'''

import random

from ..gameobjects.particle import Particle

COLOR = 0xFF00FF00


class ParticleManager():
    '''
    A class to manage particles.
    '''

    def __init__(self):
        self.particles = []

    def update(self, delta_time):
        '''
        Updates all the particles.
        '''

        self.cull_particles()

        for particle in self.particles:
            particle.update(delta_time)

    def render(self, renderer):
        '''
        Renders all the particles.
        '''
        for particle in self.particles:
            particle.render(renderer)

    def create_explosion(self, point: tuple):
        '''
        Creates an explosion.
        '''
        for _ in range(20):
            radius = random.randint(3, 5)
            velocity = (random.randint(-100, 100), random.randint(-100, 100))
            angular_velocity = random.randint(10, 50)
            lifetime = random.randint(1000, 3000)  # milliseconds
            particle = Particle(point, radius, velocity,
                                angular_velocity, COLOR, lifetime)
            self.particles.append(particle)

    def cull_particles(self):
        '''
        Removes dead particles.
        '''
        self.particles = [
            particle for particle in self.particles if not particle.dead]

    def reset(self):
        '''
        Resets the particle manager.
        '''
        self.particles = []
