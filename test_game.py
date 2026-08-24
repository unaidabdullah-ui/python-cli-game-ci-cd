"""Unit tests for game.py"""

from unittest.mock import patch

import pytest

from game import evaluate_guess, generate_target, play_game


class TestEvaluateGuess:
    def test_low(self):
        assert evaluate_guess(3, 7) == "low"

    def test_high(self):
        assert evaluate_guess(9, 7) == "high"

    def test_correct(self):
        assert evaluate_guess(7, 7) == "correct"


class TestGenerateTarget:
    def test_within_bounds(self):
        for _ in range(100):
            target = generate_target(1, 10)
            assert 1 <= target <= 10

    def test_invalid_range_raises(self):
        with pytest.raises(ValueError):
            generate_target(10, 1)

    @patch("game.random.randint", return_value=5)
    def test_uses_randint(self, mock_randint):
        assert generate_target(1, 10) == 5
        mock_randint.assert_called_once_with(1, 10)


class TestPlayGame:
    @patch("builtins.input", side_effect=["5"])
    @patch("game.generate_target", return_value=5)
    def test_correct_first_try(self, mock_target, mock_input, capsys):
        attempts = play_game()
        assert attempts == 1
        assert "Congratulations" in capsys.readouterr().out

    @patch("builtins.input", side_effect=["1", "9", "5"])
    @patch("game.generate_target", return_value=5)
    def test_multiple_attempts(self, mock_target, mock_input, capsys):
        attempts = play_game()
        assert attempts == 3
        out = capsys.readouterr().out
        assert "Too low!" in out
        assert "Too high!" in out

    @patch("builtins.input", side_effect=["abc", "5"])
    @patch("game.generate_target", return_value=5)
    def test_invalid_input_is_ignored(self, mock_target, mock_input, capsys):
        attempts = play_game()
        assert attempts == 1
        assert "Please enter a valid integer." in capsys.readouterr().out

    @patch("builtins.input", side_effect=["1", "2"])
    @patch("game.generate_target", return_value=5)
    def test_max_attempts_exceeded_raises(self, mock_target, mock_input):
        with pytest.raises(RuntimeError):
            play_game(max_attempts=2)
