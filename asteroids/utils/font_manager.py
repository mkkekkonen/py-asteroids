'''
The font_manager module contains the FontManager class,
which is used to load and manage fonts.
'''

from sdl2 import sdlttf


class FontManager():
    '''
    The FontManager class is used to load and manage fonts.
    '''

    def __init__(self):
        self.fonts = {
            'menu': sdlttf.TTF_OpenFont(b'Orbitron.ttf', 24),
            'game': sdlttf.TTF_OpenFont(b'Orbitron.ttf', 36),
            'small': sdlttf.TTF_OpenFont(b'Orbitron.ttf', 18)
        }

    def dispose(self):
        '''
        Disposes of the fonts.
        '''

        for font in self.fonts.values():
            sdlttf.TTF_CloseFont(font)
