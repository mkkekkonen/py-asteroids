'''
This module containes the ServiceLocator class, which is used to register
and get services.
'''

MIXER = 'mixer'
FONT_MANAGER = 'font_manager'
QUIT_FLAG_CONTAINER = 'quit_flag_container'
BULLET_MANAGER = 'bullet_manager'
PARTICLE_MANAGER = 'particle_manager'
GAME_STATE_MANAGER = 'game_state_manager'
STATS_MANAGER = 'stats_manager'


class ServiceLocator:
    '''
    The ServiceLocator class is used to register and get services.
    '''

    _services = {}

    @classmethod
    def register(cls, name, service):
        '''
        Registers a service with the service locator.
        '''
        cls._services[name] = service

    @classmethod
    def get(cls, name):
        '''
        Gets a service from the service locator.
        '''
        return cls._services[name]
