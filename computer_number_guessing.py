import random


def greet():
    print('''****** Welcome to the number guessing game ******
            The computer will guess a random number and you will have to tell that 
            whether the guessed number is correct or not!
    ''')


def guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low
        feedback = input(f"Is {computer_guess} too high(H), too low(L) or correct(c)?").lower()
        if feedback == 'h':
            high = computer_guess - 1
        elif feedback == 'l':
            low = computer_guess + 1
    print("Hurrah! computer guessed the number correctly!")


def again():
    while True:
        choice = input("Do you want to play again? (Yes/No) \n").lower()
        if choice == "yes":
            upper_limit = int(input("Enter the upper limit for guessing range: "))
            guess(upper_limit)
        elif choice == "no":
            print("Ok bye! Thank you for playing with me. 😊")
            break
        else:
            print("Please enter a valid choice.")


greet()
upper_limit = int(input("Enter the upper limit for guessing range: "))
guess(upper_limit)
again()