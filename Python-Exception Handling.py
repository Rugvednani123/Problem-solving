class BankAccount:

    def __init__(self, balance):
        self.__balance = balance
        self.__closed = False

    def deposit(self, amount):
        try:
            if self.__closed:
                raise Exception("Account is closed")

            if amount <= 0:
                raise Exception("Deposit amount must be greater than zero")

            self.__balance = self.__balance + amount
            print("Amount deposited successfully")

        except Exception as e:
            print("Error:", e)

    def withdraw(self, amount):
        try:
            if self.__closed:
                raise Exception("Account is closed")

            if amount <= 0:
                raise Exception("Withdrawal amount must be greater than zero")

            if amount > self.__balance:
                raise Exception("Insufficient funds")

            self.__balance = self.__balance - amount
            print("Amount withdrawn successfully")

        except Exception as e:
            print("Error:", e)

    def check_balance(self):
        try:
            if self.__closed:
                raise Exception("Account is closed")

            print("Current Balance:", self.__balance)

        except Exception as e:
            print("Error:", e)

    def close_account(self):
        self.__closed = True
        print("Account closed successfully")


def main():

    account = BankAccount(1000)

    print("----- Normal Deposit -----")
    account.deposit(500)
    account.check_balance()

    print("\n----- Normal Withdrawal -----")
    account.withdraw(200)
    account.check_balance()

    print("\n----- Insufficient Funds -----")
    account.withdraw(5000)

    print("\n----- Negative Deposit -----")
    account.deposit(-100)

    print("\n----- Negative Withdrawal -----")
    account.withdraw(-200)

    print("\n----- Non-numeric Amount -----")
    try:
        account.deposit("abc")
    except Exception as e:
        print("Error: Invalid amount")

    print("\n----- Closing Account -----")
    account.close_account()

    print("\n----- Operation After Closing -----")
    account.deposit(500)
    account.withdraw(100)
    account.check_balance()


main()