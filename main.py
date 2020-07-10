#!/usr/bin/env python3
import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main() -> None:
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        "tileset10x10.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Game test",
        vsync=True,

    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")   # Changes order of x and y variables in numpy, which by default accesses 2D arrays in [y,x] order
        while True:  # Game loop
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)  # This actually updates the screen with what we told it to (I think)

            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


print("Hello World!")

# This line explained in detail:
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do/419185#419185
if __name__ == "__main__":
    main()
