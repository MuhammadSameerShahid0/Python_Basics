# Design an abstract class ATM with methods withdraw, deposit, and check_balance. Implement this class in a subclass UserATM and simulate user interaction.

from abc import abstractmethod, ABC


class ATM(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def withdraw(self):
        return self.amount

    @abstractmethod
    def deposit(self):
        return self.amount

    @abstractmethod
    def check_balance(self):
        return self.amount


class UserATM(ATM):
    def __init__(self, amount):
        super().__init__(amount)

    def run(self):
        while True:
            choice = input("Choose: [1] Deposit, [2] Withdraw, [3] Balance, [4] Exit: ")
            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid option.")

    def withdraw(self):  # Forced to add these method cuz it's an abstractmethod in ATM
        try:
            withdraw_amount = int(input("Enter the amount to withdraw: "))
            if withdraw_amount > self.amount:
                print("You don't have enough money!")
            else:
                self.amount -= withdraw_amount
                print(f"You have withdrawn! {withdraw_amount} and remaining balance is {self.amount}")
        except Exception as ex:
            print("Error: ", ex)

    def deposit(self):  # Forced to add these method cuz it's an abstractmethod in ATM
        try:
            deposit_amount = int(input("Enter the amount to deposit: "))
            if deposit_amount < 0:
                print("Sorry -ve amount can't be deposit")
            else:
                self.amount += deposit_amount
                print(f"You have deposited: {deposit_amount} and new balance is {self.amount}")
        except Exception as ex:
            print("Error: ", ex)

    def check_balance(self):  # Forced to add these method cuz it's an abstractmethod in ATM
        print(f"Your balance is {self.amount}")


userATM = UserATM(100)
userATM.run()
