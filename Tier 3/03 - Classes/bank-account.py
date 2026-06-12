class BankAccount:
  def __init__(self, account_holder: str, balance: float):
    self.account_holder = account_holder
    self.balance = balance

  def deposit(self, amount: int):
    self.balance += amount
    print(f"You have successfully deposited ${amount}")
    print(f"Your balance now is: ${self.balance}")

  def withdraw(self, amount: int):
    if amount > self.balance:
      print("You don't have enough to withdraw, therefore the money has not been deducted")
      print(f"Your balance now is: ${self.balance}")
    else:
      self.balance -= amount    
      print(f"You have successfully withdrawn ${amount}")
      print(f"Your balance now is: ${self.balance}")

# Test cases
test = BankAccount("Lemon", 0)
test.deposit(15)
test.withdraw(12)
test.deposit(100)
test.withdraw(120)
test.withdraw(50)