class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, phone, email, address):
        if name not in self.contacts:
            self.contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
            print(f'Contact {name} added successfully.')
        else:
            print('Contact already exists. Use update to modify details.')

    def view(self):
        if not self.contacts:
            print('Contact list is empty.')
        else:
            print('Contact List:')
            for name, details in self.contacts.items():
                print(f"{name}: {details['Phone']}")

    def search(self, keyword):
        results = []
        for name, details in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in details['Phone']:
                results.append((name, details))
        return results

    def update(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
            print(f'Contact {name} updated successfully.')
        else:
            print('Contact not found. Use add to add a new contact.')

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f'Contact {name} deleted successfully.')
        else:
            print('Contact not found. Cannot delete.')

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact_book.add(name, phone, email, address)

        elif choice == '2':
            contact_book.view()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = contact_book.search(keyword)
            if results:
                print("Search Results:")
                for name, details in results:
                    print(f"{name}: {details}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            address = input("Enter new address: ")
            contact_book.update(name, phone, email, address)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete(name)

        elif choice == '6':
            print("Exiting Contact Book.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
