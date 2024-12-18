# A simple contact book program

# This is the phonebook where we'll store all contacts.
# The name will be the key, and the phone number will be the value.
phonebook = {}

# Function to show the menu options to the user
def show_menu():
    print("\n--- Contact Book ---")
    print("1. Add a Contact")
    print("2. Search for a Contact")
    print("3. Update a Contact")
    print("4. Delete a Contact")
    print("5. Show All Contacts")
    print("6. Exit")

# Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    if name in phonebook:  # Check if the contact already exists
        print(f"{name} already exists in the phonebook.")
    else:
        phone = input("Enter the phone number: ")
        phonebook[name] = phone  # Add the contact to the phonebook
        print(f"{name} has been added.")

# Function to search for a contact
def search_contact():
    name = input("Enter the contact's name to search for: ")
    if name in phonebook:  # Check if the contact exists
        print(f"{name}'s phone number is {phonebook[name]}.")
    else:
        print(f"{name} is not in the phonebook.")

# Function to update a contact
def update_contact():
    name = input("Enter the contact's name to update: ")
    if name in phonebook:  # Check if the contact exists
        new_phone = input("Enter the new phone number: ")
        phonebook[name] = new_phone  # Update the phone number
        print(f"{name}'s phone number has been updated.")
    else:
        print(f"{name} is not in the phonebook.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the contact's name to delete: ")
    if name in phonebook:  # Check if the contact exists
        del phonebook[name]  # Remove the contact from the phonebook
        print(f"{name} has been deleted.")
    else:
        print(f"{name} is not in the phonebook.")

# Function to show all contacts in alphabetical order
def show_all_contacts():
    if phonebook:  # Check if there are any contacts
        print("\nContacts in the phonebook:")
        for name in sorted(phonebook):  # Sort contacts alphabetically
            print(f"{name}: {phonebook[name]}")
    else:
        print("The phonebook is empty.")

# Main program loop
while True:
    show_menu()  # Show the menu to the user
    choice = input("Choose an option (1-6): ")  # Get the user's choice

    # Perform the action based on the user's choice
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        show_all_contacts()
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break  # Exit the loop and program
    else:
        print("Invalid choice. Please try again.")
