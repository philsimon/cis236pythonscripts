"""Track shooting statistics across several basketball games."""


def ask_int(prompt, minimum=0, maximum=None):
    """Prompt until the user enters a whole number within the limits."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if value < minimum:
            print(f"Enter {minimum} or more.")
        elif maximum is not None and value > maximum:
            print(f"Enter {maximum} or fewer.")
        else:
            return value


def percentage(makes, shots):
    """Return the shooting percentage, or 0 when no shots were taken."""
    return makes / shots * 100 if shots else 0.0


def print_grid(games):
    """Print one row per game plus an aggregate summary row."""
    header = f"{'Game':<10}{'Shots':>8}{'Makes':>8}{'Misses':>8}{'FG%':>8}"
    rule = "-" * len(header)
    print()
    print(header)
    print(rule)

    total_shots = total_makes = 0
    for number, (shots, makes) in enumerate(games, start=1):
        total_shots += shots
        total_makes += makes
        print(
            f"{number:<10}{shots:>8}{makes:>8}{shots - makes:>8}"
            f"{percentage(makes, shots):>7.1f}%"
        )

    print(rule)
    print(
        f"{'Total':<10}{total_shots:>8}{total_makes:>8}"
        f"{total_shots - total_makes:>8}"
        f"{percentage(total_makes, total_shots):>7.1f}%"
    )


def main():
    num_games = ask_int("How many games did you play? ", minimum=1)

    games = []
    for game in range(1, num_games + 1):
        shots = ask_int(f"Game {game}: how many shots did you take? ")
        makes = ask_int(f"Game {game}: how many did you make? ", maximum=shots)
        games.append((shots, makes))

    print_grid(games)


if __name__ == "__main__":
    main()
