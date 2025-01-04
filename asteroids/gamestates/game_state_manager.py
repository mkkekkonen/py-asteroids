'''
This module is responsible for managing the game states.
'''

from .game_state import GameState


class GameStateManager():
    '''
    This class is responsible for managing the game states.
    '''

    def __init__(self):
        self.states = {
            'game': GameState(),
        }
        self.current_state = 'game'

    def set_state(self, state_name):
        '''
        Sets the current state of the game.
        '''
        self.current_state = state_name
        self.states[self.current_state].reset()

    def update(self, delta_time: float):
        '''
        Updates the current game state.
        '''
        self.states[self.current_state].update(delta_time)

    def render(self, renderer):
        '''
        Renders the current game state.
        '''
        self.states[self.current_state].render(renderer)

    def handle_events(self, event):
        '''
        Handles events for the current game state.
        '''
        self.states[self.current_state].handle_events(event)
