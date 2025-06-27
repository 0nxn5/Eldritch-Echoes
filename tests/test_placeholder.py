"""Simple tests for the Game class."""

from pathlib import Path
import sys

# Ensure the src package is discoverable when running tests directly with ``pytest``.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.game import Game


def test_game_runs(capsys):
    game = Game()
    game.run()
    captured = capsys.readouterr()
    assert "Starting Eldritch Echoes" in captured.out
