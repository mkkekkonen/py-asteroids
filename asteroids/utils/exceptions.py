'''
This module contains custom exceptions that are raised in the game.
'''


class MixerInitializationError(Exception):
    '''Exception raised for errors in the initialization of the SDL2 mixer.'''

    def __init__(self, message='Failed to initialize mixer'):
        self.message = message
        super().__init__(self.message)
