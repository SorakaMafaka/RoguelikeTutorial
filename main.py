#!/usr/bin/env python3
# This class handles setting up screen size, tileset etc and creating the entities
import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler


def main() -> None:
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "tileset10x10.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width /2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    engine = Engine(entities=entities, event_handler=event_handler, player=player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Game test",
        vsync=True,

    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")   # Changes order of x and y variables in numpy, which by default accesses 2D arrays in [y,x] order
        while True:  # Game loop
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)

            #context.present(root_console)  # This actually updates the screen with what we told it to (I think)

            
# TODO: Create a GameMap

print("Hello World!")

# This line explained in detail:
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do/419185#419185
if __name__ == "__main__":
    main()
