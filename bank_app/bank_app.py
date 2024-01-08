################## CAGLA YAGMUR ICER #############
################## 19360859027 ###################
import os

class Account:
    def __init__(self, account_type, account_name, balance):
        self.account_type = account_type
        self.account_name = account_name
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Cannot be negative")
        self._balance = value

class SavingAccount(Account):
    def __init__(self, account_type, account_name, balance):
        super().__init__(account_type, account_name, balance)
        self.transaction = Transaction(self, 0)

    def calculate_balance_on_close(self):
        self.balance -= self.balance * 0.1
        return self.balance

class NormalAccount(Account):
    def __init__(self, account_type, account_name, balance):
        super().__init__(account_type, account_name, balance)
        self.transaction = Transaction(self, 0)
    
    def calculate_balance_on_close(self):
        return self.balance

class Transaction:
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def paraDondur(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print(f"Balance: {args[0].account.balance} | Transaction Amount: {args[0].amount} | Transaction Type: {func.__name__} | Account name: {args[0].account.account_name} | Account Type: {args[0].account.account_type}")
            return args[0].amount
        return wrapper

    @paraDondur   
    def paraCek(self):
        if self.account.balance - self.amount < 0:
            raise ValueError("Insufficient Balance")    
        self.account.balance -= self.amount
        self.amount = -self.amount

    @paraDondur
    def paraEkle(self):
        self.account.balance += self.amount

def paraGuncelle(transaction, choice):
    if choice == "4":
        transaction.paraCek()
    if choice == "5":
        transaction.paraEkle()
    
def create_account(account_type, account_name, balance):
    if account_type == "Saving":
        return SavingAccount(account_type, account_name, balance)
    elif account_type == "Normal":
        return NormalAccount(account_type, account_name, balance)

def close_account(account, accounts):
    account.calculate_balance_on_close()
    accounts.remove(account)
    print(f"{account.account_type} type {account.account_name} account has been closed. Balance: {account.balance}")

def save_accounts(accounts):
    with open("accounts.txt", "w") as file:
        for account in accounts:
            file.write(f"{account.account_type},{account.account_name},{account.balance}\n")

def load_accounts():
    accounts = []
    if not os.path.exists("accounts.txt"):
        with open("accounts.txt", "w") as file:
            file.write("")
        return accounts
    else:
        with open("accounts.txt", "r") as file:
            for line in file:
                account_type, account_name, balance = line.split(",")
                balance = float(balance)
                account = create_account(account_type, account_name, balance)
                accounts.append(account)
    return accounts

## Opsiyonel :)
def unique_name_check(account_name, accounts):
    for account in accounts:
        if account.account_name == account_name:
            raise ValueError("This account name is already in use. Choose a different name.")

def print_all_accounts(accounts):
    for account in accounts:
        print(f"Account name: {account.account_name} | Account Type: {account.account_type} | Balance: {account.balance}")

def get_account_by_name(account_name, accounts):
    for account in accounts:
        if account.account_name == account_name:
            return account
    raise ValueError("Could not find an account with this name")

def main():
    first_start_flag = True
    while True:
        if first_start_flag:
            accounts = load_accounts()
            first_start_flag = False

        print("""\n\t<--- MENU --->\n
        1. Create account
        2. Close account
        3. Save accounts
        4. Withdraw
        5. Deposit
        6. Print all accounts
        7. Exit
        """)
        choice = input("Choice: ")

        if choice == "1":
            while True:
                account_type = input("\nChoose account type \n1-Saving \n2-Normal \n(1/2):  ")
                if account_type not in ["1", "2"]:
                    print("\n! Please enter 1 for Saving Account and 2 for Normal Account.\n")
                    continue
                else:
                    if account_type == "1":
                        account_type = "Saving"
                    elif account_type == "2":
                        account_type = "Normal"
                    break               
            try:
                account_name = input("Account name: ")
                unique_name_check(account_name, accounts)
                balance = float(input("Balance: "))
                account = create_account(account_type, account_name, balance)
                accounts.append(account)
                input("> Account created. Press enter to continue...")
            except ValueError as error:
                print(error)
        elif choice == "2":
            account_name = input("Account name: ")
            try:
                account = get_account_by_name(account_name, accounts)
                close_account(account, accounts)
            except ValueError as error:
                print(error)
                continue
            input("\n> Press enter to continue...")
        elif choice == "3":
            save_accounts(accounts)
            accounts = load_accounts()
            input("> Accounts are saved on file. Press enter to reload...")
            continue
        elif choice == "4":
            try:
                account_name = input("> Enter the Account Name and press enter: ")
                amount = input("> Enter the amount you want to withdraw: ")
                amount = float(amount)
                account = get_account_by_name(account_name, accounts)
                transaction = Transaction(account, amount)
                paraGuncelle(transaction, choice)
                input("\n> Press enter to continue...")
            except ValueError as error:
                print(error)
                continue   
        elif choice == "5":
            try:
                account_name = input("Account name: ")
                amount = input("Amount: ")
                amount = float(amount)
                account = get_account_by_name(account_name, accounts)
                transaction = Transaction(account, amount)
                paraGuncelle(transaction, choice)
                input("\n> Press enter to continue...")
            except ValueError as error:
                print(error)
                continue 
        elif choice == "6":
            print_all_accounts(accounts)
            input("\n> All accounts were successfully printed to the screen. Press enter to continue...")
        elif choice == "7":
            break
        else:
            print("\n> You made an undefined selection. Please try again.")

if __name__ == "__main__":
    main()