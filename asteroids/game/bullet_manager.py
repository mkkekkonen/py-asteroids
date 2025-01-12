'''
This module is responsible for managing the bullets in the game.
'''

from asteroids.gameobjects.bullet import Bullet


class BulletManager():
    '''
    This class is responsible for managing the bullets in the game.
    '''

    def __init__(self):
        self.bullets = []

    def render(self, renderer):
        '''
        Renders all the bullets.
        '''

        for bullet in self.bullets:
            bullet.render(renderer)

    def update(self, delta_time):
        '''
        Updates all the bullets.
        '''

        self.bullets = [
            bullet for bullet in self.bullets if not bullet.is_dead()]
        for bullet in self.bullets:
            bullet.update(delta_time)

    def create_bullet(self, position: tuple, velocity: tuple, rotation: int, color: int):
        '''
        Creates a new bullet.
        '''

        self.bullets.append(Bullet(position, velocity, rotation, color))

    def reset(self):
        '''
        Resets the bullet manager.
        '''

        self.bullets = []
