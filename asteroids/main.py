import sys
import sdl2.ext
import sdl2

from .game import Game


def main():
    '''
    The main function of the game.
    '''

    sdl2.ext.init()
    window = sdl2.ext.Window("Hello World!", size=(800, 600))
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
