import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = [random.choice(COLORS) for _ in range(CODE_LENGTH)]
    return code

def guess_code():
    while True:
        guess = input("Guess (e.g. R G B Y): ").upper().split()
        
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        if all(color in COLORS for color in guess):
            return guess
        else:
            print(f"Invalid colors in your guess. Valid colors are: {COLORS}")

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0
    used_indices = []

    # Count correct positions first
    for i in range(CODE_LENGTH):
        if guess[i] == real_code[i]:
            correct_pos += 1
            used_indices.append(i)
        else:
            color_counts[real_code[i]] = color_counts.get(real_code[i], 0) + 1

    # Then count correct colors in wrong position
    for i in range(CODE_LENGTH):
        if guess[i] != real_code[i] and color_counts.get(guess[i], 0) > 0:
            incorrect_pos += 1
            color_counts[guess[i]] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to Mastermind! You have {TRIES} tries to guess the code.")
    print("Valid colors are:", ', '.join(COLORS))
    print(f"Enter your guess as space-separated colors (e.g. R G B Y).")

    code = generate_code()

    for attempt in range(1, TRIES + 1):
        print(f"\nAttempt {attempt}")
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"🎉 You guessed the code in {attempt} tries! Code: {' '.join(code)}")
            break

        print(f"Correct Positions: {correct_pos} | Correct Colors (wrong pos): {incorrect_pos}")

    else:
        print("\n❌ You ran out of tries.")
        print("The correct code was:", ' '.join(code))

if __name__ == "__main__":
    game()
