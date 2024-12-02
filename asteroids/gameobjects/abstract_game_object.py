'''
This module contains the AbstractGameObject class, which is
an abstract class that all game objects should inherit from.
'''

ERROR_MESSAGE = "Subclasses must implement this method"


class AbstractGameObject():
    '''
    This is an abstract class that all game objects should inherit from.
    '''

    def __init__(self):
        pass

    def render(self, renderer):
        '''
        Renders the game object.
        '''
        raise NotImplementedError(ERROR_MESSAGE)

    def update(self):
        '''
        Updates the game object's position and velocity.
        '''
        raise NotImplementedError(ERROR_MESSAGE)

    def handle_events(self, event):
        '''
        Handles events for the game object.
        '''
        raise NotImplementedError(ERROR_MESSAGE)
