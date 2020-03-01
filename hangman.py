from typing import Any, List, Type
from random import choice

MAX_TURNS = 10
SECRET_WORD = ''
guesses = []


def new_game() -> None:
    """Start a new game by asking for the player name and printing the rules."""
    while True:
        player = input('Enter your name: ')
        if player.isalnum():
            break
    print(f"Hello, {player}", "Let's play Hangman!")
    print('RULES:',
          '1. You have 10 turns to guess the secret word.',
          '2. Each turn you can enter only 1 letter',
          '3. You win by guessing all the correct letters within 10 turns', 'Good Luck!\n', sep='\n')


def get_secret_word() -> str:
    """Read from text file into list and then pick a random item from that list"""
    words = []
    with open('game_words.txt', 'r', encoding='utf-8', newline='') as f:
        words.extend(f.read().splitlines())
    return choice(words).upper()


def print_turns_used(turns: int) -> None:
    """Print out the remaining turns player has left."""
    print(f'TURNS: {turns}/{MAX_TURNS}\n')


def display_secret(secret: str) -> None:
    """Print the secret word using underscores to display missing letters"""
    for letter in secret:
        if letter in guesses:
            print(letter.upper(), end=' ')
        else:
            print('_', end=' ')
    print('\n')


def get_input() -> str:
    """Get user input and make sure it is valid. Then print the correct response"""
    while True:
        guess = input('Enter Letter: ').upper()
        if len(guess) != 1:
            print('Enter Only A Single Letter!')
        elif (guess < 'a' or guess > 'z') or (guess < 'A' or guess > 'Z'):
            print('Alphabetical Characters Only! (a-z)')
        elif guess in guesses:
            print(f'Letter "{guess}" Already Chosen!')
        else:
            return guess


def player_guess() -> None:
    """Main driver function. Deals with getting user input and deciding if the player has won or lost"""
    turns = MAX_TURNS
    print(f'Your word is {len(SECRET_WORD)} letters long\n')
    while turns > 0:
        fails = 0
        for char in SECRET_WORD:
            if char not in guesses:
                fails += 1
        if fails == 0:
            end_game(True)
            return
        print_turns_used(turns)
        display_secret(SECRET_WORD)
        guess = get_input()

        guesses.append(guess)
        if guess in SECRET_WORD:
            print('CORRECT!')
        else:
            print('INCORRECT...')
            turns -= 1
    end_game(False)


def end_game(winner: bool) -> None:
    """Print winning or losing message and clear variables in case player wants to play again"""
    if winner:
        print(
            'WINNER!', f'You guessed the secret word: {SECRET_WORD}')
    else:
        print('YOU LOSE!', f'The secret word was: {SECRET_WORD}')
    guesses.clear()


if __name__ == '__main__':
    new_game()
    while True:
        SECRET_WORD = get_secret_word()
        player_guess()
        if input('Would you like to play again? (Y/N) ')[0].upper() != 'Y':
            break
