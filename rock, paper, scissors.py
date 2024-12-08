import random
entity = ["rock","paper","scissors"]
computer_choice = random.choice(entity)

def greet():
    print("************ Welcome to Rock, Paper, Scissors Game **************")

def get_user_choice():
    u_choice = input('''What do you want to choose?
          There are three options...
          1- Rock
          2- Paper
          3- Scissors\n''').lower()
    return u_choice
    
def cmp_choice_prnt():
    print(f"My choice is {computer_choice}.")
    return computer_choice

def game(user,computer):
    if user==computer:
        print("It's a tie! ")
    elif (computer == "rock" and  user == "scissors") or (computer == "paper" and  user == "rock") or (computer == "scissors" and user == "paper"):
        print("Computer wins and you lost! ")
    else:
        print("Great! You win.")

def again():
    while(True):
        choice = input("Do you want to play again? ").lower()
        if choice == "yes":
            GAME()
        if choice == "no":
            print("OK BYE! Nice to play with you...")
        break
        
def GAME():
    greet()
    user=get_user_choice()
    computer=cmp_choice_prnt()
    game(user,computer)
    again()
GAME()