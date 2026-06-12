# 1. Create a list named 'contacts' with at least 4 contacts.
# Each contact will be represented as a list with name, phone, and email.
contacts = [
    ['Alice', '555-1234', 'alice@email.com'],
    ['Bob', '555-5678', 'bob@email.com'],
    ['Charlie', '555-8765', 'charlie@email.com'],
    ['Diana', '555-4321', 'diana@email.com']
]

# 2. Print the details of the second contact.
# Output will be: ['Bob', '555-5678', 'bob@email.com']
print("\nSecond contact:")
print(contacts[1])

# 3. Update the phone number of the third contact.
contacts[2][1] = '555-9999'
print("\nAfter updating Charlie's phone number:")
print(contacts[2])

# 4. Add a new contact to the list.
new_contact = ['Ethan', '555-3812', 'ethan@email.com']
contacts.append(new_contact)
print("\nAfter adding new contact:")
print(contacts[-1])  # Print the last added contact

# 5. Print the updated contact list.
print("\nUpdated contact list:")
print("{:<10} {:<12} {:<20}".format("Name", "Phone", "Email"))
print("-" * 40)
for contact in contacts:
    print("{:<10} {:<12} {:<20}".format(contact[0], contact[1], contact[2]))