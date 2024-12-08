from words import nouns
import random
import string


def greet():
    print('''
    Hello!
    Welcome to the Hangman Game.
    *************  **************
    ''')


def word(words):
    secret_word = random.choice(nouns)
    length = len(secret_word)
    spaces = ''
    for letter in range(length):
        spaces += '_'
    print(spaces)
    lives = len(secret_word)
    guesses = set()
    while spaces != secret_word and lives > 0:
        user_input = input("Enter any guess letter: ").lower()
        new_display = ''
        if len(user_input) == 1:
            if user_input in guesses:
                print("You have entered that letter already. Guess a new one.")
                continue
            guesses.add(user_input)
            if user_input in secret_word:
                for i in range(length):
                    if secret_word[i] == user_input:
                        new_display += user_input
                    else:
                        new_display += spaces[i]
                spaces = new_display
            else:
                lives -= 1
                print(f"You have {lives} lives left!")
            print(spaces)
        else:
            print("Please enter only a single letter!")
    if spaces == secret_word:
        print("Congratulations! You guessed the word correctly.")
    else:
        print(f"Ahh! You lost. The word was: {secret_word}")


def again():
    while True:
        choice = input("Do you want to play again? (Yes/No)\n").lower()
        if choice == "yes":
            word(nouns)
        elif choice == 'no':
            print("Ok bye! It was good to play with you.")
            break
        else:
            print("Please enter a valid choice! ")


greet()
word(nouns)
again()


