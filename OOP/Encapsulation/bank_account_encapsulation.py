#Create a BankAccount class with private variables for balance. Add methods to deposit, withdraw, and check balance using getter/setter methods. Prevent negative withdrawals.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_current_balance(self):
            balance  = 100
            self.__balance = balance
            return balance

    def deposit(self):
        add_amount = int(input("Enter the amount to deposit: "))

        try:
            if add_amount < 0:
                return  "Sorry -ve amount can't be deposit"
            else:
                new_balance = self.__balance + add_amount
                print(self.__balance)
                return f"Deposited {add_amount} successfully in your account, balance: {new_balance}"
        except Exception as ex:
            print("Exception: ", ex)

    def withdraw(self):
        withdraw_amount = int(input("Enter the amount to withdraw: "))
        try:
            if withdraw_amount > self.__balance:
                return "Insufficient balance"
            else:
                self.__balance -= withdraw_amount
                return f"Withdraw {withdraw_amount} successfully debit, remaining balance: {self.__balance}"
        except Exception as ex:
            print("Exception: ", ex)


class ATM(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def verification(self):
        pin = int(input("Enter your 4-digit pin: "))
        if pin == 1234: #Mock Pin
            print("Access granted. Welcome to the ATM!")
            print(
                '''
                --- Choose the option ---
                
                    1. Deposit
                    2. Withdraw
                    3. Check balance
                '''
            )
            options = int(input("Enter your option: "))
            match options:
                case 1:
                    print(super().deposit())
                case 2:
                    print(super().withdraw())
                case 3:
                    print(super().get_current_balance())
                case _:
                    print("Entered option does not exist")
        else:
            print("Entered pin not correct")

obj_atm = ATM(100)
obj_atm.verification()
