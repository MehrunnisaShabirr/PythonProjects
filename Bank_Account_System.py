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
                    print(f"Amount deposited successfully. Your new balance is {self.account_balance} (❁´◡`❁)")
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
                        print(f"Withdrawal successful. Take your cash 💵. New balance: {self.account_balance} (❁´◡`❁)")
                        break
                    else:
                        print(f"Insufficient balance. Your current balance is {self.account_balance}.")
                        break
                else:
                    print("Please enter a positive amount to withdraw.")
            except ValueError:
                print("Please enter a valid integer amount.")

    def current_balance(self):
        print(f"Your current balance is {self.account_balance}")

    def choice(self):
        while True:
            try:
                user_choice = int(input('''What do you want to do?
1. Deposit amount
2. Withdraw amount
3. Check balance
0. Exit
Your choice: '''))

                if user_choice == 1:
                    self.deposit()
                elif user_choice == 2:
                    self.withdraw()
                elif user_choice == 3:
                    self.current_balance()
                elif user_choice == 0:
                    print("Thank you for using our service. Goodbye! (*^_^*)")
                    break
                else:
                    print("Please enter a valid option (0-3).")
            except ValueError:
                print("Please enter a valid integer option.")

# Initialize default accounts
account1 = BankAccount("Mehrunnisa", 555, 5000)
account2 = BankAccount("Qasim", 123, 2000)
account3 = BankAccount("Amna", 456)
account4 = BankAccount("Ali", 789, 100)

accounts = {
    account1.account_number: account1,
    account2.account_number: account2,
    account3.account_number: account3,
    account4.account_number: account4,
}

def create_account():
    name = input("Enter the account holder's name: ").strip().lower()
    while True:
        try:
            number = int(input("Enter the account number (digits only): "))
            if number in accounts:
                print("This account number already exists. Please choose a different number.")
            else:
                new_account = BankAccount(name, number)
                accounts[number] = new_account
                print(f"Account created successfully for {name.title()} with account number {number}.")
                new_account.choice()
                break
        except ValueError:
            print("Please enter a valid integer for the account number.")

def login():
    while True:
        name = input("Enter your name: ").strip().lower()
        try:
            number = int(input("Enter your account number: "))
            if number in accounts and accounts[number].account_name == name:
                print(f"Welcome back, {name.title()}!")
                accounts[number].choice()
                break
            else:
                print("Incorrect name or account number. Please try again.")
        except ValueError:
            print("Please enter a valid integer for the account number.")

def main():
    while True:
        try:
            user_choice = int(input('''Welcome to the Bank.
What do you want to do?
1. Create a new account
2. Login to existing account
0. Exit
Your choice: '''))

            if user_choice == 1:
                create_account()
            elif user_choice == 2:
                login()
            elif user_choice == 0:
                print("Thank you for using our service. Bye!")
                break
            else:
                print("Please enter a valid option (0-2).")
        except ValueError:
            print("Please enter a valid integer option.")

if __name__ == "__main__":
    main()
