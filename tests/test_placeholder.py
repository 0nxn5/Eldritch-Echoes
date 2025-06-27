from src.core.game import Game


def test_game_runs(capsys):
    game = Game()
    game.run()
    captured = capsys.readouterr()
    assert "Starting Eldritch Echoes" in captured.out
