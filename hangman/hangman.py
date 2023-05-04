"""
Hangman Game

This program is a simple implementation of the Hangman game. The game is played by guessing letters to complete a secret word, with a limited number of attempts. The game supports loading a custom dictionary file and selecting a word to guess by its index in the file.

Usage:
Run the program in the command line using Python 3. For the best experience, make sure to use a terminal that supports ANSI escape codes.

Features:
- Customizable dictionary file
- Selection of a word to guess by its index in the file
- Colorful text output using the colorama and termcolor modules
- Debug mode for developers to print messages to the console
- Welcome screen loaded from a file
- Interactive gameplay with user input and feedback

Module Dependencies:
- os
- colorama
- termcolor
- ex6
- ex7
- ex8
- ex9

Author:
Tamir David, May 4th, 2023

"""
import os
from colorama import init   # Importing required modules
from termcolor import colored
from ex6 import try_update_letter_guessed
from ex7 import show_hidden_word, check_win
from ex8 import print_hangman
from ex9 import choose_word

# Dictionary for text coloring
COLOR_CODE = {
    "INSTRUCTIONS": 'yellow',
    "INVALID_INPUT": ('red', ['bold']),
    "WORD": 'green',
    "HANGMAN": ('cyan', ['bold']),
    "WELCOME": 'blue',
    "RESULT": ('blue', ['bold']),
    "DEBUG": 'magenta'
}

DEBUG_LOGGING = False
DEFAULT_DICTIONARY = "dictionary.txt"
WELCOME_SCREEN_FILE = "welcome_screen.txt"


def print_debug(message):
    """
    Helper function to print debug messages.
    """
    if DEBUG_LOGGING:
        print(colored(message, COLOR_CODE["DEBUG"]))


def print_err_input(message):
    """
    Helper function to print error messages.
    """
    print(colored(message, COLOR_CODE["INVALID_INPUT"]))


def main():
    """
    Main function that runs the game.
    """
    with open(WELCOME_SCREEN_FILE, 'r') as welcome_file:  # Open and print the welcome screen file
        print(colored(welcome_file.read(), COLOR_CODE["WELCOME"]))

    MAX_TRIES = 7   # Set the maximum number of tries

    # Prompt the user for the file path until it is valid
    while True:
        text_file_path = input("Enter file path: ")
        if os.path.exists(text_file_path):
            break
        print_err_input("Invalid file path. Please try again.")

    # Prompt the user for the index until it is valid
    while True:
        index_str = input("Enter index: ")
        if index_str.isdigit() and int(index_str)>0:
            secret_word_index = int(index_str)
            break
        print_err_input("Invalid index. Please enter a positive integer.")

    print_debug("1. Process input = {0} {1}".format(text_file_path, secret_word_index))

    try:
        secret_word = choose_word(text_file_path, secret_word_index)[1]   # Get the secret word
    except ValueError:
        try:
            text_file_path = DEFAULT_DICTIONARY
            secret_word = choose_word(text_file_path, secret_word_index)[1]
        except ValueError:
            print_err_input("Couldn't choose_word from {0} index {1}".format(text_file_path, secret_word_index))
            return
    print_debug("2. Generate secret = {0}".format(secret_word))

    old_letters_guessed = []   # Initialize the list of guessed letters
    print(colored("Let's start!", COLOR_CODE["WELCOME"]))

    num_of_tries = 1   # Set the number of tries to 1
    while num_of_tries <= MAX_TRIES:
        hangman_picture = print_hangman(num_of_tries)   # Print the hangman picture
        print(colored(hangman_picture, COLOR_CODE["HANGMAN"]))

        if num_of_tries == MAX_TRIES:   # Check if the maximum number of tries is reached
            print_debug("Lose condition met {0} = {1}".format(num_of_tries, MAX_TRIES))
            print(colored("LOST", COLOR_CODE["RESULT"]))
            break

        hidden_word = show_hidden_word(secret_word, old_letters_guessed)   # Get the hidden word
        print(colored(hidden_word, COLOR_CODE["WORD"]))

        if check_win(secret_word, old_letters_guessed):
            print_debug("Win condition met - all secret word letters guessed")
            print(colored("WON", COLOR_CODE["RESULT"]))
            break

        letter_guessed = input("Guess a letter: ").lower()

        while not try_update_letter_guessed(letter_guessed, old_letters_guessed):
            print(colored("X", COLOR_CODE["INVALID_INPUT"]))
            letter_guessed = input("Guess a letter: ").lower()

        if letter_guessed not in secret_word:
            num_of_tries += 1

    print(colored("The word was {0}".format(secret_word), COLOR_CODE["RESULT"]))
    print_debug("3. Exiting main")


if __name__ == '__main__':
    init()
    main()
