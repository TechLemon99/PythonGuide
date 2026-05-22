class BankAccount:
    def __init__(self, account_number: str, owner_name: str, initial_balance: float = 0.0):
        self.__account_number = account_number
        self.__owner_name = owner_name
        self.__balance = max(0.0, initial_balance)

    # Getter methods
    def get_account_number(self) -> str:
        return self.__account_number

    def get_owner_name(self) -> str:
        return self.__owner_name

    def get_balance(self) -> float:
        return self.__balance

    # Setter methods
    def set_owner_name(self, new_name: str):
        if isinstance(new_name, str) and len(new_name.strip()) > 0:
            self.__owner_name = new_name.strip()
        else:
            print("Error: Owner name must be a non-empty string")

    # Transaction methods
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Error: Deposit amount must be positive")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive")
        elif amount > self.__balance:
            print(f"Error: Insufficient funds. Current balance: ${self.__balance:.2f}")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")

    def __str__(self):
        return (f"Bank Account - {self.__account_number}\n"
                f"Owner: {self.__owner_name}\n"
                f"Balance: ${self.__balance:.2f}")