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

chosen_letters = []
word = random.choice(word_list)
word_length = len(word)
body_parts = 5
display = ['*'] * word_length

def check_for_same_guess(guess):
    if guess in chosen_letters:
        print("You've already choosen this letter.")
        new_guess = get_guess()
    else:
        chosen_letters.append(guess)
        return True
            
def get_user_input(prompt):
    # get user input
    return input(prompt)

def validate_input(user_input):
    # validate user input
    if len(user_input) == 1 and user_input.isalpha():
        return user_input
    raise ValueError("Invalid input. Please enter a single letter.")

def get_guess():
    while True:
        try:
            guess = validate_input(get_user_input("Guess a letter: "))
            return guess
        except ValueError as e:
            print(e)

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

def main():
    # main game loop
    global display
    while True:
        guess = get_guess()
        check_for_same_guess(guess)
        is_correct(guess)
        print_result(is_correct(guess))
        update_body_parts(is_correct(guess))
        display = update_display(guess, word, display)
        print(" ".join(display))
        if "*" not in display:
            print("You win!")
            break

main()

# def check_for_same_guess(guess, chosen_letters):
#     if guess in chosen_letters:
#         print("You've already chosen this letter.")
#         return False
#     else:
#         chosen_letters.append(guess)
#         return True

# # Usage example
# chosen_letters = []
# while True:
#     guess = input("Enter a letter: ")
#     if check_for_same_guess(guess, chosen_letters):
#         # Process the new guess
#         break
#     # If False is returned, the loop will continue, asking for a new guess
