'''
The main module of the game. This module is responsible for
initializing the game and running the game loop.
'''

import sys
import sdl2.ext
import sdl2
import sdl2.sdlmixer
import sdl2.sdlttf

from .game import Game


def main():
    '''
    The main function of the game.
    '''

    mixer_flags = (sdl2.sdlmixer.MIX_INIT_MP3 |
                   sdl2.sdlmixer.MIX_INIT_OGG)

    sdl2.ext.init()

    ttf_result = sdl2.sdlttf.TTF_Init()
    if ttf_result != 0:
        return ttf_result

    mix_result = sdl2.sdlmixer.Mix_Init(mixer_flags)
    if mix_result != mixer_flags:
        return mix_result

    window = sdl2.ext.Window("Asteroids", size=(800, 600))
    window.show()

    game = Game(window)

    game_time = sdl2.SDL_GetTicks()

    running = True
    while running:
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            game.handle_events(event)

        current_time = sdl2.SDL_GetTicks()
        delta_time = current_time - game_time

        game.render()
        game.update(delta_time)
        window.refresh()

        if delta_time < 1000 / 60:
            sdl2.SDL_Delay(int((1000 / 60) - delta_time))

        game_time = current_time

    sdl2.ext.quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
