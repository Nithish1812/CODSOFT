def nithish_contact_hub():
    # We use a dictionary to store contacts: {Name: Phone}
    contacts = {}

    print("=" * 40)
    print("      NITHISH-CONTACTHUB (CLI)      ")
    print("=" * 40)

    while True:
        print("\n1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ")

        if choice == '1':
            name = input("Enter Name: ").strip().title()
            phone = input("Enter Phone Number: ").strip()
            contacts[name] = phone
            print(f" Contact '{name}' added successfully!")

        elif choice == '2':
            if not contacts:
                print(" Your contact book is empty.")
            else:
                print("\n--- ALL CONTACTS ---")
                for name, phone in contacts.items():
                    print(f"👤 {name}: {phone}")

        elif choice == '3':
            search_name = input("Enter name to search: ").strip().title()
            if search_name in contacts:
                print(f" Found: {search_name} - {contacts[search_name]}")
            else:
                print(" Contact not found.")

        elif choice == '4':
            del_name = input("Enter name to delete: ").strip().title()
            if del_name in contacts:
                del contacts[del_name]
                print(f" Contact '{del_name}' deleted.")
            else:
                print(" Contact not found.")

        elif choice == '5':
            print("Thank you for using Nithish-ContactHub! Goodbye. 👋")
            break
        
        else:
            print(" Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    nithish_contact_hub()