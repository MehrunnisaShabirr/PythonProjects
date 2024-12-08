class BankAccount:
    def __init__(self, ac_name, ac_number, balance=0):
        self.account_name = ac_name.lower()
        self.account_number = ac_number
        self.account_balance = balance

    def deposit(self):
        while True:
            try:
                dep_amount = int(input("Enter the amount you want to deposit: "))
                if dep_amount > 0:
                    self.account_balance += dep_amount
                    print(f"Your amount is deposited successfully. Now your balance is {self.account_balance} (❁´◡`❁)")
                    break
                else:
                    print("Please enter a positive amount to deposit.")
            except ValueError:
                print("Please enter a valid integer amount.")

    def withdraw(self):
        while True:
            try:
                withdraw_amount = int(input("Enter the amount you want to withdraw: "))
                if withdraw_amount > 0:
                    if withdraw_amount <= self.account_balance:
                        self.account_balance -= withdraw_amount
                        print(f"Your amount is withdrawn. Here is your cash💵. Now your balance is {self.account_balance} (❁´◡`❁)")
                        break
                    else:
                        print(f"You do not have enough money. Your net balance is only {self.account_balance}.")
                        break
                else:
                    print("Please enter a positive amount to withdraw.")
            except ValueError:
                print("Please enter a valid integer amount.")

    def current(self):
        print(f"Your current balance is {self.account_balance}")

    def choice(self):
        while True:
            try:
                user_choice = int(input('''What do you want to do?
                Press 1 to deposit amount
                Press 2 to withdraw amount
                Press 3 to check net balance
                Press 0 to exit
                '''))

                if 0 <= user_choice < 4:
                    match user_choice:
                        case 1:
                            self.deposit()
                        case 2:
                            self.withdraw()
                        case 3:
                            self.current()
                        case 0:
                            print("Thank you for using our service. Goodbye! (*^_^*)")
                            break
                else:
                    print("Please enter a valid option (0-3).")
            except ValueError:
                print("Please enter an integer value.")


# Initialize accounts
account1 = BankAccount("Mehrunnisa", 555, 5000)
account2 = BankAccount("Qasim", 123, 2000)
account3 = BankAccount("Amna", 456)
account4 = BankAccount("Ali", 789, 100)

# Store accounts in a dictionary
accounts = {
    account1.account_number: account1,
    account2.account_number: account2,
    account3.account_number: account3,
    account4.account_number: account4,
}


def create_account():
    name = input("Enter the account holder's name: ").lower()
    while True:
        try:
            number = int(input("Enter the account number: "))
            if number in accounts:
                print("An account with this number already exists. Please choose a different number.")
            else:
                new_account = BankAccount(name, number)
                accounts[number] = new_account
                print(f"Account created successfully for {name} with account number {number}.")
                new_account.choice()
                break
        except ValueError:
            print("Please enter a valid integer for the account number.")

def login():
    while True:
        name = input("Enter your name: ").lower()
        try:
            number = int(input("Enter the account number: "))
            if number in accounts and accounts[number].account_name == name:
                accounts[number].choice()
                break
            else:
                print("Account with this number does not exist or the name is incorrect. Please try again.")
        except ValueError:
            print("Please enter a valid integer for the account number.")


def main():
    while True:
        try:
            user_choice = int(input('''Welcome to the Bank.
                What do you want to do?
                Press 1 to create a new account.
                Press 2 to login to your existing account.
                Press 0 to exit.
                '''))

            if 0 <= user_choice < 3:
                match user_choice:
                    case 1:
                        create_account()
                    case 2:
                        login()
                    case 0:
                        print("Thank you for using our service. Bye.")
                        break
            else:
                print("Invalid value entered. Please enter a valid value.")
        except ValueError:
            print("Invalid value entered. Please enter a valid value.")


main()
