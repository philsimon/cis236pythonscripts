"""Calculate the winning streak needed to reach a target win percentage."""

from fractions import Fraction
from math import ceil


def streak_needed(wins, games, target_pct):
    """Return the consecutive wins needed to reach target_pct.

    Solves (wins + x) / (games + x) = target for x, which gives
    x = (target * games - wins) / (1 - target).
    """
    target = Fraction(str(target_pct)) / 100
    if target >= 1:
        raise ValueError("Target must be below 100 percent.")
    x = (target * games - wins) / (1 - target)
    return max(0, ceil(x))


def main():
    wins = int(input("Games won: "))
    games = int(input("Games played: "))
    target_pct = input("Target winning percentage: ")

    if not 0 <= wins <= games or games == 0:
        print("Wins must fall between 0 and the games played.")
        return

    try:
        x = streak_needed(wins, games, target_pct)
    except ValueError as error:
        print(error)
        return

    if x == 0:
        print("You already meet that percentage.")
    else:
        print(f"You need to win {x} games in a row to reach {target_pct} percent.")


if __name__ == "__main__":
    main()
