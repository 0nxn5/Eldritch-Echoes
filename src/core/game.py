"""Core game engine implementation."""

from __future__ import annotations

import time


class Game:
    """Basic game class skeleton."""

    def __init__(self) -> None:
        self.running = False

    def process_input(self) -> None:
        """Handle user input.

        This method will later capture keyboard or mouse events. For now it
        simply acts as a placeholder so the game loop is easy to extend.
        """

    def update(self) -> None:
        """Update the game state."""

    def render(self) -> None:
        """Render the current game state."""

    def run(self, frame_limit: int = 1) -> None:
        """Start the main game loop.

        Parameters
        ----------
        frame_limit:
            Number of iterations to run the loop. Keeping this small ensures
            tests execute quickly and prevents an infinite loop during early
            development.
        """

        print("Starting Eldritch Echoes...")
        self.running = True

        frames = 0
        while self.running and frames < frame_limit:
            self.process_input()
            self.update()
            self.render()

            frames += 1
            time.sleep(0.01)
