
from random import randint

from colorama import Fore, Back, Style


# Have a list of secret words.
secret_dictionary = ['adult', 'affix', 'afoot']
size_of_dictionary = len(secret_dictionary) - 1

# Randomly choose a word from the random dictionary
# secret_word = secret_dictionary[randint(0, size_of_dictionary)]
secret_word = secret_dictionary[0]

size_secret_word = 5
guess_list = ["_ _ _ _ _"]
letter_array = []
color_list = []

# The letter array contains the truth. Are the guesses identifying correct letters?
# The entire word that was guessed needs to be printed, while secretly checking if it matches
# letters in the secret word.


# Wordle requires that each guess be five letters.
# If guess is less or more than a length of five letters, block.
# If guess is not within the word bank, do not allow it.
# 6 full guesses are allowed.

class Main:
    def __init__(self):
        self.number_of_guesses = 6

    def start_game(self):
        for each in range(0, size_secret_word):
            letter_array.append("_")

    def modify_letters_displayed(self):
        pass

    def take_in_guess(self):
        guess = input("\nPlease guess a five letter word: ")
        if (len(guess) != 5):
            Main.take_in_guess(self)
        if guess == secret_word and self.number_of_guesses > 0:
            Main.cycle_through_letters(self, guess)
            # Main.print_current_letters(self)
            print(Style.RESET_ALL + "\nYOU WIN!!")
            exit()
        else:
            guess_list.append(guess)
            self.number_of_guesses = self.number_of_guesses - 1
            Main.cycle_through_letters(self, guess)
            # Main.print_current_letters(self)
            # print(guess_list, end="\n")

    def cycle_through_letters(self, guess):
        for each in range(0, 5):
            if guess[each] == secret_word[each]:
                letter_array[each] = guess[each]
                print(Back.GREEN + guess[each], end=" ")
            else:
                print(Back.BLACK + guess[each], end=" ")
        print(Style.RESET_ALL)


game = Main()
game.start_game()
# game.print_current_letters()
while game.number_of_guesses > 0:
    game.take_in_guess()

print('YOU LOSE')
