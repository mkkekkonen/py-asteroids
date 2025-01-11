'''
The GameStatsManager class is responsible for managing the game statistics.
'''


class GameStatsManager():
    '''
    This class is responsible for managing the game statistics.
    '''

    def __init__(self):
        self.time = 0

    def reset(self):
        '''
        Resets the game statistics.
        '''
        self.time = 0

    def update(self, delta_time):
        '''
        Updates the game statistics.
        '''
        self.time += delta_time
