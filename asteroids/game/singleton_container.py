
from .bullet_manager import BulletManager


class SingletonContainer():
    '''
    This class is used to store all the singletons in the game.
    '''

    def __init__(self):
        self.singletons = {
            'BulletManager': BulletManager.get_instance()
        }

    @staticmethod
    def get_instance():
        '''
        Returns the instance of the SingletonContainer.
        '''

        if not hasattr(SingletonContainer, 'instance'):
            SingletonContainer.instance = SingletonContainer()
        return SingletonContainer.instance

    def get_singleton(self, singleton_key: str):
        '''
        Returns the singleton instance of the specified class.
        '''

        return self.singletons.get(singleton_key)
