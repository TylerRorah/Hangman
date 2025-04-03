import random
import json

class Hangman():

    def __init__(self):
        # Initialize game attributes
        self.chosen_letters = set()
        self.word = word_list.random
        self.body_parts = 6
        self.attempts = 0
        self.display = len(word)
        self.get_guess()


    def main(self):
        while self.attempts < self.body_parts:
            self.guess = get_guess(self.chosen_letters)

    def get_guess(self):
        guess = input("Guess a letter: ").lower().strip()
        if guess in self.chosen_letters:
            print("You've already chosen this letter!")
        else:


if __name__ == "__main__":
    with open("wordlist.json", "r") as file:
        word_list = json.load(file)
    