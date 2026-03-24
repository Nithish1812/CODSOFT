import random

def nithish_pygame():
    # --- BRANDED HEADER & RULES ---
    print("=" * 40)
    print("       NITHISH-PYGAME (CLI)       ")
    print("=" * 40)
    print(" RULES:")
    print("  - Rock beats Scissors")
    print("  - Scissors beats Paper")
    print("  - Paper beats Rock")
    print("-" * 40)

    # Initialize Scores
    user_score = 0
    comp_score = 0

    while True:
        # 1. User Input
        print(f"\nSCORE | YOU: {user_score}  COMP: {comp_score}")
        user_choice = input("Choose Rock, Paper, or Scissors (or 'exit' to quit): ").capitalize()

        if user_choice == "Exit":
            print("\nFinal Score - YOU:", user_score, "| COMP:", comp_score)
            print("Thanks for playing Nithish-PyGame! ")
            break

        if user_choice not in ["Rock", "Paper", "Scissors"]:
            print(" Invalid choice! Please type Rock, Paper, or Scissors.")
            continue

        # 2. Computer Choice
        options = ["Rock", "Paper", "Scissors"]
        comp_choice = random.choice(options)
        print(f"Computer chose: {comp_choice}")

        # 3. Game Logic
        if user_choice == comp_choice:
            print(" IT'S A TIE!")
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            print(f" YOU WIN! {user_choice} beats {comp_choice}")
            user_score += 1
        else:
            print(f" YOU LOSE! {comp_choice} beats {user_choice}")
            comp_score += 1

        print("-" * 40)

if __name__ == "__main__":
    nithish_pygame()