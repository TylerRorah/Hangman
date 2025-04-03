import random
import json

class Hangman():

    def __init__(self, word_list):
        # Initialize game attributes
        self.chosen_letters = set()
        self.word = random.choice (word_list)
        self.body_parts = 6
        self.attempts = 0
        self.display = ['*'] * len(self.word)

    def main(self):
        while self.attempts < self.body_parts:
            guess = self.get_guess()

            if guess in self.chosen_letters:
                print(f"You've already guessed {guess}")
                continue
            
            if self.is_correct(guess):
                print("You've guessed correctly!")
                self.display = self.update_display(guess)
            else:
                print("Incorrect guess!")
                self.attempts += 1
                self.update_body_parts()
            
            print(" ".join(self.display))

            self.chosen_letters.add(guess)

            # Check win condition
            if "*" not in self.display:
                print("You win!")
                break
    
    def get_guess(self):
        while True:
            guess = input("Guess a letter: ").lower().strip()
            if len(guess) == 1 and guess.isalpha():
                return guess
            print("Invalid input. Please enter a single letter.")
    
    def is_correct(self, guess):
        return guess in self.word
             
    def update_display(self, guess):
        for i in range(len(self.word)):
            if guess == self.word[i]:
                self.display[i] = guess
        return self.display

    def update_body_parts(self):
        print(f"{self.body_parts} added")

if __name__ == "__main__":
    with open("wordlist.json", "r") as file:
        word_list = json.load(file)

    game = Hangman(word_list)
    game.main()
    