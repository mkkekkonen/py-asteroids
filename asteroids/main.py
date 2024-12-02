import sys
import sdl2.ext

from .game import Game


def main():
    sdl2.ext.init()
    window = sdl2.ext.Window("Hello World!", size=(800, 600))
    window.show()

    game = Game(window)

    running = True
    while running:
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            game.handle_events(event)

        game.render()
        window.refresh()

    sdl2.ext.quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
