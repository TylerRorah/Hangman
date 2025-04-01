def main():
    # Initialize game variables
    word = "example"  # Replace with actual word selection logic
    display = ["*"] * len(word)
    chosen_letters = set()
    max_attempts = 6  # Number of body parts in Hangman
    attempts = 0

    print("Welcome to the game!")
    print(" ".join(display))

    # Main game loop
    while attempts < max_attempts:
        guess = get_guess(chosen_letters)  # Get a valid guess from the player
        
        if guess in chosen_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue
        
        chosen_letters.add(guess)

        if is_correct(guess, word):
            print("Correct guess!")
            display = update_display(guess, word, display)
        else:
            print("Incorrect guess!")
            attempts += 1
            update_body_parts(attempts)

        print(" ".join(display))

        # Check win condition
        if "*" not in display:
            print("You win!")
            break

    # Check loss condition
    if attempts >= max_attempts:
        print("Game over! You've run out of attempts.")
        print(f"The correct word was: {word}")

# Helper functions (define these as needed)
def get_guess(chosen_letters):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        print("Invalid input. Please enter a single letter.")

def is_correct(guess, word):
    return guess in word

def update_display(guess, word, display):
    return [guess if word[i] == guess else display[i] for i in range(len(word))]

def update_body_parts(attempts):
    print(f"Body part {attempts} added!")  # Replace with actual Hangman drawing logic

# Run the game
if __name__ == "__main__":
    main()