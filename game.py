"""Guess the Number - a simple CLI game.

Game logic is separated from I/O so it can be unit tested without
mocking stdin/stdout for every case.
"""

from __future__ import annotations

import argparse
import logging
import random
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def generate_target(low: int, high: int) -> int:
    """Generate a random target number in the inclusive range [low, high]."""
    if low > high:
        raise ValueError("low must be <= high")
    return random.randint(low, high)


def evaluate_guess(guess: int, target: int) -> str:
    """Compare a guess to the target. Returns 'low', 'high', or 'correct'."""
    if guess < target:
        return "low"
    if guess > target:
        return "high"
    return "correct"


def play_game(low: int = 1, high: int = 10, max_attempts: int | None = None) -> int:
    """Run one round of the guessing game against stdin/stdout.

    Returns the number of attempts taken to guess correctly.
    Raises RuntimeError if max_attempts is exceeded without a correct guess.
    """
    target = generate_target(low, high)
    attempts = 0
    logger.debug("New round started (target hidden from player)")

    while True:
        raw = input(f"Guess a number between {low} and {high}: ")
        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1
        result = evaluate_guess(guess, target)

        if result == "low":
            print("Too low!")
        elif result == "high":
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            logger.info("Round won in %d attempts", attempts)
            return attempts

        if max_attempts is not None and attempts >= max_attempts:
            print(f"Out of attempts! The number was {target}.")
            logger.info("Round lost after %d attempts", attempts)
            raise RuntimeError("Max attempts exceeded")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Guess the Number CLI game")
    parser.add_argument("--low", type=int, default=1, help="Lower bound (inclusive)")
    parser.add_argument("--high", type=int, default=10, help="Upper bound (inclusive)")
    parser.add_argument("--max-attempts", type=int, default=None, help="Optional attempt limit")
    args = parser.parse_args(argv)

    print("Welcome to the Guessing Game!")
    try:
        play_game(low=args.low, high=args.high, max_attempts=args.max_attempts)
    except RuntimeError:
        return 1
    except KeyboardInterrupt:
        print("\nGoodbye!")
        return 130
    return 0


if __name__ == "__main__":
    sys.exit(main())
