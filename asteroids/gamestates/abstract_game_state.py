'''
Abstract class for game states.
'''


class AbstractGameState():
    '''
    Abstract class for game states.
    '''

    def __init__(self, game_state_manager):
        '''
        Initializes the game state.
        '''
        self.game_state_manager = game_state_manager

    def reset(self):
        '''
        Resets the game state.
        '''
        raise NotImplementedError

    def render(self, renderer):
        '''
        Renders the game state.
        '''
        raise NotImplementedError

    def update(self, delta_time: float):
        '''
        Updates the game state.
        '''
        raise NotImplementedError

    def handle_events(self, event):
        '''
        Handles events for the game state.
        '''
        raise NotImplementedError
