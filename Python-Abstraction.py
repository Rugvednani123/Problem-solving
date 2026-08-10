from abc import ABC, abstractmethod


# ============================================================
# ABSTRACT BASE CLASS
# ============================================================

class BankAccount(ABC):

    def __init__(self, account_number, holder_name, balance):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.account_number = account_number
        self.holder_name = holder_name
        self._balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def balance_inquiry(self):
        pass


# ============================================================
# CHECKING ACCOUNT
# ============================================================

class CheckingAccount(BankAccount):

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self._balance = self._balance + amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self._balance:
            raise ValueError("Insufficient funds.")

        self._balance = self._balance - amount
        print("Amount withdrawn successfully.")

    def balance_inquiry(self):
        return self._balance


# ============================================================
# SAVINGS ACCOUNT
# ============================================================

class SavingsAccount(BankAccount):

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self._balance = self._balance + amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        # Savings account must maintain minimum balance of 500
        if self._balance - amount < 500:
            raise ValueError(
                "Savings account must maintain minimum balance of 500."
            )

        self._balance = self._balance - amount
        print("Amount withdrawn successfully.")

    def balance_inquiry(self):
        return self._balance


# ============================================================
# BANK CLASS
# ============================================================

class Bank:

    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print("Account added successfully.")

    def find_account(self, account_number):

        for account in self.accounts:

            if account.account_number == account_number:
                return account

        raise ValueError("Account not found.")

    def deposit(self, account_number, amount):

        try:
            account = self.find_account(account_number)
            account.deposit(amount)

        except ValueError as e:
            print("Error:", e)

    def withdraw(self, account_number, amount):

        try:
            account = self.find_account(account_number)
            account.withdraw(amount)

        except ValueError as e:
            print("Error:", e)

    def show_balance(self, account_number):

        try:
            account = self.find_account(account_number)

            print("Account Number:", account.account_number)
            print("Account Holder:", account.holder_name)
            print("Balance:", account.balance_inquiry())

        except ValueError as e:
            print("Error:", e)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("======================================")
    print("     BANK ACCOUNT MANAGEMENT SYSTEM")
    print("======================================")

    # Creating Bank object
    bank = Bank()


    # --------------------------------------------------------
    # Creating Checking Account
    # --------------------------------------------------------

    print("\nCreating Checking Account...")

    checking = CheckingAccount(
        "C101",
        "Rugved",
        1000
    )

    bank.add_account(checking)


    # --------------------------------------------------------
    # Creating Savings Account
    # --------------------------------------------------------

    print("\nCreating Savings Account...")

    savings = SavingsAccount(
        "S101",
        "Rahul",
        2000
    )

    bank.add_account(savings)


    # ========================================================
    # CHECKING ACCOUNT OPERATIONS
    # ========================================================

    print("\n======================================")
    print("       CHECKING ACCOUNT")
    print("======================================")

    print("\nInitial Balance:")
    bank.show_balance("C101")


    print("\nDepositing 500:")
    bank.deposit("C101", 500)

    bank.show_balance("C101")


    print("\nWithdrawing 300:")
    bank.withdraw("C101", 300)

    bank.show_balance("C101")


    # ========================================================
    # SAVINGS ACCOUNT OPERATIONS
    # ========================================================

    print("\n======================================")
    print("        SAVINGS ACCOUNT")
    print("======================================")

    print("\nInitial Balance:")
    bank.show_balance("S101")


    print("\nDepositing 1000:")
    bank.deposit("S101", 1000)

    bank.show_balance("S101")


    print("\nWithdrawing 500:")
    bank.withdraw("S101", 500)

    bank.show_balance("S101")


    # ========================================================
    # ERROR HANDLING
    # ========================================================

    print("\n======================================")
    print("          ERROR HANDLING")
    print("======================================")


    # Insufficient funds
    print("\n1. Testing insufficient funds:")

    bank.withdraw("C101", 10000)


    # Negative deposit
    print("\n2. Testing negative deposit:")

    bank.deposit("C101", -500)


    # Negative withdrawal
    print("\n3. Testing negative withdrawal:")

    bank.withdraw("C101", -200)


    # Savings minimum balance
    print("\n4. Testing savings minimum balance:")

    bank.withdraw("S101", 5000)


    # Invalid account
    print("\n5. Testing invalid account:")

    bank.show_balance("A999")


    # ========================================================
    # DEMONSTRATING ABSTRACTION
    # ========================================================

    print("\n======================================")
    print("       ABSTRACTION DEMONSTRATION")
    print("======================================")

    print("\nThe Bank class does not need to know")
    print("whether the account is Checking or Savings.")

    print("\nCalling deposit on Checking Account:")

    bank.deposit("C101", 100)


    print("\nCalling deposit on Savings Account:")

    bank.deposit("S101", 100)


    print("\nFinal Checking Balance:")
    bank.show_balance("C101")


    print("\nFinal Savings Balance:")
    bank.show_balance("S101")


    print("\n======================================")
    print("           PROGRAM COMPLETED")
    print("======================================")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()