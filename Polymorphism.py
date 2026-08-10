# ============================================================
# BASE CLASS
# ============================================================

class PaymentMethod:

    def make_payment(self, amount):
        pass

    def get_payment_details(self):
        pass


# ============================================================
# CREDIT CARD
# ============================================================

class CreditCard(PaymentMethod):

    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def make_payment(self, amount):
        if amount <= 0:
            print("Invalid payment amount")
        else:
            print("Payment of", amount, "made using Credit Card")

    def get_payment_details(self):
        print("Payment Method: Credit Card")
        print("Card Holder:", self.card_holder)
        print("Card Number:", self.card_number)


# ============================================================
# DEBIT CARD
# ============================================================

class DebitCard(PaymentMethod):

    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def make_payment(self, amount):
        if amount <= 0:
            print("Invalid payment amount")
        else:
            print("Payment of", amount, "made using Debit Card")

    def get_payment_details(self):
        print("Payment Method: Debit Card")
        print("Card Holder:", self.card_holder)
        print("Card Number:", self.card_number)


# ============================================================
# BANK TRANSFER
# ============================================================

class BankTransfer(PaymentMethod):

    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder

    def make_payment(self, amount):
        if amount <= 0:
            print("Invalid payment amount")
        else:
            print("Payment of", amount, "made using Bank Transfer")

    def get_payment_details(self):
        print("Payment Method: Bank Transfer")
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)


# ============================================================
# DUCK TYPING FUNCTION
# ============================================================

def process_payment(payment_method, amount):

    print("\n--------------------------------")

    # We don't check whether it is
    # CreditCard, DebitCard, or BankTransfer.

    payment_method.get_payment_details()

    payment_method.make_payment(amount)

    print("--------------------------------")


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():

    print("========== PAYMENT SYSTEM ==========")

    # Creating objects

    credit_card = CreditCard(
        "1234-5678-9012-3456",
        "Rugved"
    )

    debit_card = DebitCard(
        "9876-5432-1098-7654",
        "Rahul"
    )

    bank_transfer = BankTransfer(
        "1234567890",
        "Suresh"
    )


    # Credit Card Payment

    print("\n1. CREDIT CARD PAYMENT")

    process_payment(
        credit_card,
        5000
    )


    # Debit Card Payment

    print("\n2. DEBIT CARD PAYMENT")

    process_payment(
        debit_card,
        2500
    )


    # Bank Transfer Payment

    print("\n3. BANK TRANSFER PAYMENT")

    process_payment(
        bank_transfer,
        10000
    )


    print("\n========== PROGRAM COMPLETED ==========")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()