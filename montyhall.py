
import random

def play_round():
    first = input("Pick a door (1-3): ")
    
    if first not in ('1', '2', '3'):
        print("Invalid.")
        return False
    first_idx = int(first) - 1


    car = random.randrange(3)
    monty = random.choice([i for i in range(3) if i != first_idx and i != car])

    print(f"Monty opens door {monty + 1} (goat).")
    remaining = [i for i in range(3) if i != monty]

    final = input(f"Pick your final door {tuple(d + 1 for d in remaining)}: ")
    
    if not final.isdigit() or (int(final) - 1) not in remaining:
        print("Invalid final choice.")
        return False

    final_idx = int(final) - 1
    win = final_idx == car
    print("You win!" if win else f"You lose. Car was behind door {car + 1}.")
    return win

def main():
    wins = 0
    plays = 0
    while True:
        rounds = play_round()
        if rounds is None:
            break
        if rounds is False:
            continue
        plays += 1
        wins += 1 if rounds else 0
        print(f"Score: {wins}/{plays}\n")

    if plays:
        print(f"Final: {wins}/{plays} ({wins/plays*100:.1f}%)")
    print("Goodbye.")

if __name__ == "__main__":
    main()
