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
    chosen_letters = []
    word = random.choice(word_list)
    word_length = len(word)
    body_parts = 5
    display = ['*'] * word_length
    attempts = 0
    # main game loop

    while True:
        guess = get_guess()
        while True:
            guess = input("Enter a letter: ")
            if check_for_same_guess(guess, chosen_letters):
                # Process the new guess
                break
        is_correct(guess)
        print_result(is_correct(guess))
        update_body_parts(is_correct(guess))
        display = update_display(guess, word, display)
        print(" ".join(display))

        # Check win condition
        if "*" not in display:
            print("You win!")
            break

        # Check lose condition
        if body_parts >= attempts:
            print ("You have lost the game, whomp whomp.")
            print ("The correct word was: {word}")

def check_for_same_guess(guess, chosen_letters):
    if guess in chosen_letters:
        print("You've already choosen this letter.")
        return False
    else:
        chosen_letters.append(guess)
        return True

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

def is_correct(guess):
    for i in range(len(word)):
        if guess == word[i]:
            return 'perfect'
    return 'no bueno'

def print_result(is_correct):
    if is_correct == 'perfect':
        print("You're one smart cookie!")
    else:
        print("Nice try but nope")

def update_body_parts(is_correct):
    global body_parts
    if is_correct == 'perfect':
        print ("You keep all your body parts")
    else:
        body_parts -= 1
        print (f"You have {body_parts} body parts left!")

main()