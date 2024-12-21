phonebook = {}

def add_contact():
    name = input("Enter the contact's name: ")
    if name in phonebook:  
        print(f"{name} already exists in the phonebook.")
    else:
        phone = input("Enter the phone number: ")
        phonebook[name] = phone  
        print(f"{name} has been added.")

def search_contact():
    name = input("Enter the contact's name to search for: ")
    if name in phonebook:  
        print(f"{name}'s phone number is {phonebook[name]}.")
    else:
        print(f"{name} is not in the phonebook.")

def update_contact():
    name = input("Enter the contact's name to update: ")
    if name in phonebook:  
        new_phone = input("Enter the new phone number: ")
        phonebook[name] = new_phone  
        print(f"{name}'s phone number has been updated.")
    else:
        print(f"{name} is not in the phonebook.")

def delete_contact():
    name = input("Enter the contact's name to delete: ")
    if name in phonebook:  
        del phonebook[name] 
        print(f"{name} has been deleted.")
    else:
        print(f"{name} is not in the phonebook.")

def show_all_contacts():
    if phonebook:  
        print("\nContacts in the phonebook:")
        for name in sorted(phonebook):  
            print(f"{name}: {phonebook[name]}")
    else:
        print("The phonebook is empty.")

def show_menu():
    print("\n--- Contact Book ---")
    print("1. Add a Contact")
    print("2. Search for a Contact")
    print("3. Update a Contact")
    print("4. Delete a Contact")
    print("5. Show All Contacts")
    print("6. Exit")

while True:
    show_menu()  
    choice = input("Choose an option (1-6): ")  

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
        break  
    else:
        print("Invalid choice. Please try again.")
