# Encapsulation is about bundling data (attributes) and methods together while restricting direct access to some of the object's data.
# We use private variables (by convention, with _ or __) and getter/setter methods.

class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        print(f"Deposited {amount}, New Balance: {self._balance}")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        print(f"Withdrew {amount}, New Balance: {self._balance}")

    def get_balance(self):
        return self._balance

# Usage
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
# print(account.__balance)  # ❌ Error: Can't access private attribute

# Key point: Keeps data safe from accidental modification.