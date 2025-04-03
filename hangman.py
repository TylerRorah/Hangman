# For now, it will be a number of 5 then we can implement a visual and body parts later.
# allow the user to choose if they want to guess another letter or guess the entire word, you know cause thats the chad thing to do
# update the json to contain actual words that i can use. this is a stupid fucking easy tasks dont overthink it dumbass
# encapsulate game logic in a class
# Add Error Handling for File Operations
# can't guess same letter more than once
# can't go negative on body parts
# pick a genre of words from urban dict

import json
import random

with open("wordlist.json", "r") as file:
        word_list = json.load(file)



def main():
    # Instantiate Game Variables
    chosen_letters = set()
    word = random.choice(word_list)
    body_parts = 6
    display = ['*'] * len(word)
    attempts = 0

    # main game loop
    while attempts < body_parts:
        guess = get_guess(chosen_letters)

        if guess in chosen_letters:
            print(f"You've already guessed {guess}")
            continue

        if is_correct(guess, word):
            print("Correct guess!")
            display = update_display(guess, word, display)
        else:
            print("Incorrect guess!")
            attempts += 1
            update_body_parts(attempts)

        print(" ".join(display))

        chosen_letters.add(guess)

        # Check win condition
        if "*" not in display:
            print("You win!")
            break

    # Check lose condition
    if body_parts >= attempts:
        print ("You have lost the game, whomp whomp.")
        print (f"The correct word was: {word}")

def get_guess(chosen_letters):
    while True:
        guess = input("Enter a letter: ").lower().strip()
        if len(guess) == 1 and guess.isalpha():
            return guess
        print("Invalid input. Please enter a single letter.")

def update_display(guess, word, display):
    # update display
    for i in range(len(word)):
        if guess == word[i]:
            display[i] = guess
    return display

def is_correct(guess, word):
    return guess in word

def update_body_parts(attempts):
    print(f"{attempts} added")

if __name__ == "__main__":
    main()