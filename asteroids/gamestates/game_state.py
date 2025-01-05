from .abstract_game_state import AbstractGameState

from ..gameobjects.ship import Ship
from ..game.asteroid_generator import AsteroidGenerator
from ..game.bullet_manager import BulletManager


class GameState(AbstractGameState):
    '''
    This class represents the game state.
    '''

    def __init__(self, game_state_manager):
        super().__init__(game_state_manager)

        self.ship = None
        self.asteroids = None

        self.reset()

    def reset(self):
        '''
        Resets the game state.
        '''
        self.ship = Ship((400, 300), 20, 0, 0, 0)
        self.asteroids = AsteroidGenerator().generate(5)

    def render(self, renderer):
        '''
        Renders the game state.
        '''
        renderer.clear()

        self.ship.render(renderer.renderer)

        for asteroid in self.asteroids:
            asteroid.render(renderer.renderer)

        BulletManager.get_instance().render(renderer.renderer)

        renderer.present()

    def update(self, delta_time: float):
        '''
        Updates the game state.
        '''
        self.asteroids = [
            asteroid for asteroid in self.asteroids if not asteroid.is_dead()]
        for asteroid in self.asteroids:
            asteroid.update(delta_time)

        self.handle_bullet_collisions()

        BulletManager.get_instance().update(delta_time)

    def handle_events(self, event):
        '''
        Handles events for the game state.
        '''
        self.ship.handle_events(event)

    def handle_bullet_collisions(self):
        '''
        Handles collisions between bullets and asteroids.
        '''
        for asteroid in self.asteroids:
            for bullet in BulletManager.get_instance().bullets:
                if asteroid.is_point_inside(bullet.position):
                    asteroid.hit()
                    bullet.destroy()
