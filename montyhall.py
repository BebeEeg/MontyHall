
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Monty Hall Problem Simulation
# company: ZLI
# datetime24h: Tue Nov 11 2025 15:14:42
# username: bebee
# weeknumber: 46
# workspacename: 11_KW46_python
# year: 2025
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random

def play_round():
    # Get player's first door choice
    first = input("Pick a door (1-3): ")
    
    # Validate input
    if first not in ('1', '2', '3'):
        print("Invalid.")
        return False
    first_idx = int(first) - 1

    # Randomly place car behind one of the 3 doors
    car = random.randrange(3)

    # Monty reveals a goat (not player's choice, not the car)
    monty = random.choice([i for i in range(3) if i != first_idx and i != car])
    print(f"Monty opens door {monty + 1} (goat).")

    # Get remaining doors (excluding the one Monty opened)
    remaining = [i for i in range(3) if i != monty]

    # Get player's final door choice
    final = input(f"Pick your final door {tuple(d + 1 for d in remaining)}: ")
    
     # Validate final choice is a valid remaining door
    if not final.isdigit() or (int(final) - 1) not in remaining:
        print("Invalid final choice.")
        return False

    # Check if player won
    final_idx = int(final) - 1
    win = final_idx == car
    print("You win!" if win else f"You lose. Car was behind door {car + 1}.")
    return win

def main():
    wins = 0
    plays = 0
    # Loop until player quits
    while True:
        rounds = play_round()
        if rounds is None:
            break
        
        # Skip invalid inputs
        if rounds is False:
            continue
        plays += 1
        # Track wins
        wins += 1 if rounds else 0
        print(f"Score: {wins}/{plays}\n")

    # Display final results
    if plays:
        print(f"Final: {wins}/{plays} ({wins/plays*100:.1f}%)")
    print("Goodbye.")

if __name__ == "__main__":
    main()
