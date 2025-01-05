'''
This module contains the QuitFlagContainer class.
This class is used to store a boolean flag that can
be used to signal that the game should quit.
'''


class QuitFlagContainer:
    '''
    This class is used to store a boolean flag that can
    be used to signal that the game should quit.
    '''

    def __init__(self):
        self.quit_flag = False

    @staticmethod
    def get_instance():
        '''
        Returns the singleton instance of the QuitFlagContainer class.
        '''
        if not hasattr(QuitFlagContainer, 'instance'):
            QuitFlagContainer.instance = QuitFlagContainer()
        return QuitFlagContainer.instance

    def set_quit_flag(self):
        '''
        Sets the quit flag to True.
        '''
        self.quit_flag = True

    def get_quit_flag(self):
        '''
        Returns the value of the quit flag.
        '''
        return self.quit_flag
