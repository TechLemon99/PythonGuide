def checkUsername(username: str) -> bool:

    # Rule 1: Length check
    if len(username) > 8:
        return False

    # Rule 2: Only letters allowed (no numbers, spaces, or symbols)
    if not username.isalpha():
        return False

    # Rule 3: '<' must not be present
    if '<' in username:
        return False

    return True

# Example usage
print(checkUsername("Alice"))      # ✅ True
print(checkUsername("John123"))    # ❌ False (contains numbers)
print(checkUsername("TooLongName"))# ❌ False (too long)
print(checkUsername("Bad<Name"))   # ❌ False (contains '<')
print(checkUsername("Anna"))       # ✅ True
print(checkUsername("MARTIN"))     # ✅ True
print(checkUsername("jay!"))       # ❌ False (symbol not allowed)