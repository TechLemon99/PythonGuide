from bank_account import BankAccount

def test_account(account: BankAccount):
    print("\n" + "="*40)
    print(f"Testing account: {account.get_account_number()}")
    print("-"*40)
    
    # Test getters
    print(f"Original owner: {account.get_owner_name()}")
    print(f"Original balance: ${account.get_balance():.2f}")
    
    # Test setters and transactions
    account.set_owner_name("New Owner Name")
    print(f"Updated owner: {account.get_owner_name()}")
    
    print("\nTransaction Tests:")
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(400)  # Should fail (overdraw)
    account.deposit(-100)  # Should fail (negative deposit)
    
    print("\nFinal account status:")
    print(account)

# Create two account instances
account1 = BankAccount("ACC123456", "John Doe", 1000.00)
account2 = BankAccount("ACC789012", "Jane Smith", 500.00)

# Test both accounts
test_account(account1)
test_account(account2)

# Additional edge case testing
print("\n" + "="*40)
print("Edge Case Testing")
print("-"*40)
account3 = BankAccount("ACC000000", "Test User", -100)  # Should default to 0 balance
print(account3)
account3.deposit(0)  # Invalid
account3.withdraw(0)  # Invalid