# Create a class BankAccount with deposit and withdraw methods. Create a child class SavingsAccount with a method to calculate interest.

class BankAccount:
    def __init__(self, amount):
        self.amount = amount

    def deposit(self):
        amount = input(f"Amount deposited: ")
        self.amount = amount

    def withdraw(self):
        amount = input(f"Amount withdrawn: ")
        self.amount = amount


class SavingsAccount(BankAccount):
    def __init__(self, amount = None):
        super().__init__(amount) #Base_Class

    def deposit_or_withdraw(self):
        deposit_or_withdraw = input("Deposit or Withdraw? (d/w) ")
        if deposit_or_withdraw == "d":
            self.deposit()
        elif deposit_or_withdraw == "w":
            self.withdraw()
        else:
            print(f"Invalid input {deposit_or_withdraw}")

    def calculate_interest(self):
        try:
            interest_amount = (float(self.amount) * 0.05) * 1
            print(f"Interest amount: {interest_amount}")
        except Exception as ex:
            print(f"Error occurs: {ex}")


result = SavingsAccount()

result.deposit_or_withdraw()
result.calculate_interest()
