
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Monty Hall Problem Simulation
# company: ZLI
# datetime24h: Wed Nov 26 2025 11:33:17
# username: bebee
# weeknumber: 48
# workspacename: 11_KW46_python
# year: 2025
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random
from typing import Optional

def play_round() -> Optional[bool]:
    """Play one Monty Hall round.
    Return True for win, False for loss, None to quit.
    """
    first = input("Pick a door (1-3) or 'q' to quit: ").strip().lower()
    if first == "q":
        return None
    if first not in {"1", "2", "3"}:
        print("Invalid choice.")
        return False

    first_idx = int(first) - 1
    car = random.randrange(3)
    # Monty opens a goat door different from the player's pick and the car
    monty = random.choice([i for i in range(3) if i != first_idx and i != car])
    print(f"Monty opens door {monty + 1} (goat).")

    remaining = [i for i in range(3) if i != monty]
    final = input(f"Pick your final door {tuple(d + 1 for d in remaining)} or 'q' to quit: ").strip().lower()
    if final == "q":
        return None
    if final not in {str(d + 1) for d in remaining}:
        print("Invalid final choice.")
        return False

    final_idx = int(final) - 1
    win = final_idx == car
    print("You win!" if win else f"You lose. Car was behind door {car + 1}.")
    return win

def main() -> None:
    """Run rounds until the player quits and show the score."""
    wins = plays = 0
    while True:
        result = play_round()
        if result is None:
            break
        # Count only valid rounds (win or loss)
        plays += 1
        if result:
            wins += 1
        print(f"Score: {wins}/{plays} ({wins / plays * 100:.1f}%)\n")

    if plays:
        print(f"Final: {wins}/{plays} ({wins / plays * 100:.1f}%)")
    print("Goodbye.")

if __name__ == "__main__":
    main()
