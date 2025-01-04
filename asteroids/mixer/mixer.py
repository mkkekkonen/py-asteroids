'''
This module handles audio output.
'''

import sdl2.sdlmixer
from ..utils.exceptions import MixerInitializationError


class Mixer():
    '''
    This class handles audio output.
    '''

    def __init__(self):
        mixer_result = sdl2.sdlmixer.Mix_OpenAudioDevice(
            44100, sdl2.AUDIO_S16, 2, 1024, None, 0
        )

        if mixer_result != 0:
            raise MixerInitializationError()

        self.music = sdl2.sdlmixer.Mix_LoadMUS(b'music.ogg')
        if not self.music:
            raise MixerInitializationError()

        self.audio_files = {
            'laser': sdl2.sdlmixer.Mix_LoadWAV(b'laser.mp3'),
            'explosion': sdl2.sdlmixer.Mix_LoadWAV(b'explosion.ogg')
        }

    @staticmethod
    def get_instance():
        '''
        Returns the singleton instance of the Mixer class.
        '''

        if not hasattr(Mixer, 'instance'):
            Mixer.instance = Mixer()
        return Mixer.instance

    def play_music(self):
        '''
        Plays the music.
        '''

        sdl2.sdlmixer.Mix_PlayMusic(self.music, -1)

    def play_sound(self, sound: str):
        '''
        Plays a sound.
        '''

        sdl2.sdlmixer.Mix_PlayChannel(-1, self.audio_files[sound], 0)

    def dispose(self):
        '''
        Disposes of the mixer.
        '''

        sdl2.sdlmixer.Mix_FreeMusic(self.music)
        for sound in self.audio_files.values():
            sdl2.sdlmixer.Mix_FreeChunk(sound)
        sdl2.sdlmixer.Mix_CloseAudio()
