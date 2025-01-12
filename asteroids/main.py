'''
The main module of the game. This module is responsible for
initializing the game and running the game loop.
'''

import sys
import sdl2.ext
import sdl2
import sdl2.sdlmixer
import sdl2.sdlttf

from .mixer.mixer import Mixer
from .gamestates import GameStateManager
from .utils.font_manager import FontManager
from .game.quit_flag import QuitFlagContainer
from .game.bullet_manager import BulletManager
from .game.particle_manager import ParticleManager
from .game.game_stats_manager import GameStatsManager
from .service_locator.service_locator import (ServiceLocator, MIXER, FONT_MANAGER,
                                              QUIT_FLAG_CONTAINER, BULLET_MANAGER,
                                              PARTICLE_MANAGER, GAME_STATE_MANAGER,
                                              STATS_MANAGER)


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

    sdl2.SDL_StartTextInput()

    window = sdl2.ext.Window("Asteroids", size=(800, 600))
    window.show()

    renderer = sdl2.ext.Renderer(window, flags=sdl2.SDL_RENDERER_SOFTWARE)

    ServiceLocator.register(MIXER, Mixer())
    ServiceLocator.register(FONT_MANAGER, FontManager())
    ServiceLocator.register(QUIT_FLAG_CONTAINER, QuitFlagContainer())
    ServiceLocator.register(BULLET_MANAGER, BulletManager())
    ServiceLocator.register(PARTICLE_MANAGER, ParticleManager())
    ServiceLocator.register(GAME_STATE_MANAGER, GameStateManager())
    ServiceLocator.register(STATS_MANAGER, GameStatsManager())

    # mixer.play_music()

    game_time = sdl2.SDL_GetTicks()

    running = True
    while running:
        quit_flag = ServiceLocator.get(QUIT_FLAG_CONTAINER).get_quit_flag()
        if quit_flag is True:
            running = False
            break

        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            ServiceLocator.get(GAME_STATE_MANAGER).handle_events(event)

        current_time = sdl2.SDL_GetTicks()
        delta_time = current_time - game_time

        ServiceLocator.get(GAME_STATE_MANAGER).render(renderer)
        ServiceLocator.get(GAME_STATE_MANAGER).update(delta_time)
        window.refresh()

        if delta_time < 1000 / 60:
            sdl2.SDL_Delay(int((1000 / 60) - delta_time))

        game_time = current_time

    ServiceLocator.get(MIXER).dispose()
    ServiceLocator.get(FONT_MANAGER).dispose()

    sdl2.SDL_StopTextInput()
    sdl2.sdlttf.TTF_Quit()
    sdl2.sdlmixer.Mix_Quit()

    sdl2.ext.quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
