
from random import randint

from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'W ')
print(Back.RED, Fore.GREEN + 'W ')
print(Back.GREEN + 'W ')
print(Back.RED + 'what happens here')

print(Style.RESET_ALL)
print('back to normal now')

# Have a list of secret words.
secret_dictionary = ['adult', 'affix', 'afoot']
size_of_dictionary = len(secret_dictionary) - 1

# Randomly choose a word from the random dictionary
# secret_word = secret_dictionary[randint(0, size_of_dictionary)]
secret_word = secret_dictionary[0]

size_secret_word = 5
guess_list = []
letter_array = []


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

    def print_current_letters(self):
        for each in letter_array:
            print(each, end=" ")

    def modify_letters_displayed(self):
        pass

    def take_in_guess(self):
        guess = input("\nPlease guess a five letter word: ")
        if (len(guess) != 5):
            Main.take_in_guess(self)
        if guess == secret_word and self.number_of_guesses > 0:
            print("YOU WIN!")
        elif self.number_of_guesses > 0:
            guess_list.append(guess)
            self.number_of_guesses = self.number_of_guesses - 1
            Main.cycle_through_letters(self, guess)
            Main.print_current_letters(self)
            print(guess_list)

    def cycle_through_letters(self, guess):
        for each in range(0, 5):
            print(guess[each] + ' ' + secret_word[each] + '\n')
            if guess[each] == secret_word[each]:
                print('HELLO')
                letter_array[each] = guess[each]


game = Main()
game.start_game()
game.print_current_letters()
game.take_in_guess()
