import random


def user_choice():
    number_of_dice = int(input("Enter the number of dice you want to roll (1-3): "))
    return number_of_dice


def comp_choice():
    number_of_dice = random.randint(1, 3)
    print(f"The computer wants to roll {number_of_dice} dice.")
    return number_of_dice


def dice_roll():
    user_total = 0
    number_of_dice_user = user_choice()
    if 1 <= number_of_dice_user <= 3:
        print("You rolled:", end=" ")
        for _ in range(number_of_dice_user):
            dice_roll_user = random.randint(1, 6)
            print(f"{dice_roll_user}", end=" ")
            user_total += dice_roll_user
        print(f"\nYour total score is: {user_total}")

    else:
        print("Invalid input! Please enter a number between 1 and 3.")

    computer_total = 0
    number_of_dice_computer = comp_choice()
    print("Computer rolled:", end=" ")
    for _ in range(number_of_dice_computer):
        dice_roll_computer = random.randint(1, 6)
        print(f"{dice_roll_computer}", end=" ")
        computer_total += dice_roll_computer
    print(f"\nComputer's total score is: {computer_total}")

    if user_total > computer_total:
        print("You win!")
    elif user_total < computer_total:
        print("Computer wins! Give one more try to win.")
    else:
        print("It's a tie!")


def choice():
    while True:
        option = input("Do you want to play again? (Yes/No): ").lower()
        if option == 'yes':
            dice_roll()
        elif option == 'no':
            print("Thank you for playing. Bye!")
            break
        else:
            print("Please enter a valid choice. (Yes/No)")


dice_roll()
choice()