import os
import csv

def check_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone', 'Email'])

def show_menu():
    print("Menu:")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Exit")
    print()

def get_info():

    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    return name, phone, email

def add_contact(filename, name, phone, email):

    # check if file exists
    check_file(filename)

    # check duplicates 
    with open(filename, 'r', newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'].lower() == name.lower():
                print("Contact already exists.")
                return
    # then add the contact
    with open(filename, 'a', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    print("Contact added successfully.")
        
def show_contacts(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Name: {row['Name']}\nPhone: {row['Phone']}\nEmail: {row['Email']}\n")

def search_contact(filename, name):
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'].lower() == name.lower():
                print(f"Name: {row['Name']}\nPhone: {row['Phone']}\nEmail: {row['Email']}\n")
            else:
                print("Contact not found.")
if __name__ == "__main__":
    filename = "contacts.csv"
    check_file(filename)

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name, phone, email = get_info()
            add_contact(filename, name, phone, email)
        elif choice == "2":
            show_contacts(filename)
        elif choice == "3":
            contact_name = input("Enter name to search for: ")
            search_contact(filename,contact_name)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
