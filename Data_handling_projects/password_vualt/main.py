import base64
import os

def encode(text):
   return base64.b64encode(text.encode()).decode()

def decode(text):
   return base64.b64decode(text.encode()).decode()

def pass_strength_checkker(password):
    length_pass = len(password)
    pass_digi = any(char.isdigit() for char in password)
    pass_upper = any(char.isupper() for char in password)
    pass_lower = any(char.islower() for char in password)
    pass_special = any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password)

    score = sum([length_pass >= 8, pass_digi, pass_upper, pass_lower, pass_special])

    return ['weak password.', 'medium password.', 'strong password.', 'very strong password.'][score-1]

def add_credential(file_name):
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    strength = pass_strength_checkker(password)

    line = f"{website} || {username} || {password}\n"
    encoded_line = encode(line)
    with open(file_name, "a") as file:
        file.write(encoded_line + "\n")
    print("✅ Credential added successfully.")

def view_credentials(file_name):
    if not os.path.exists(file_name):
        print("No credentials found.")
        return
    with open(file_name, mode="r", encoding="utf-8") as f:
        for line in f:
            decoded_line = decode(line.strip())
            website, username, password = decoded_line.split("||")
            hidden_password = '*' * len(password)
            print(f"Website: {website.strip()}, Username: {username.strip()}, Password: {password.strip()} (Strength: {pass_strength_checkker(password.strip())})")

def update_credential(file_name):
    website = input("Enter the website to update: ")
    new_username = input("Enter the new username: ")
    new_password = input("Enter the new password: ")
    strength = pass_strength_checkker(new_password)

    with open(file_name, "r") as file:
        lines = file.readlines()
    with open(file_name, "w") as file:
        for line in lines:
            decoded_line = decode(line.strip())
            if decoded_line.startswith(website):
                updated_line = f"{website} || {new_username} || {new_password}\n"
                encoded_line = encode(updated_line)
                file.write(encoded_line + "\n")
                print("✅ Credential updated successfully.")
            else:
                file.write(line)

def delete_credential(file_name):
    website = input("Enter the website to delete: ")
    if not os.path.exists(file_name):
        print("No credentials found.")
        return
    with open(file_name, "r") as file:
        lines = file.readlines()
    with open(file_name, "w") as file:
        found = False

        for line in lines:
            decoded_line = decode(line.strip())
            if decoded_line.startswith(website):
                found = True
                print(f"✅ Credential for {website} deleted successfully.")
            else:
                file.write(line)

        if not found:
            print(f"No credential found for {website}.")


def show_menu():
    print("\n--- Credential Vault Menu ---")

    print("1. Add Credential")
    print("2. View Credentials")
    print("3. Update Credential")
    print("4. Delete Credential")
    print("5. Exit")


if __name__ == "__main__":
    # Define the path to the file
    file_path = "vault.txt"
    while True:

        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_credential(file_name=file_path)
        elif choice == "2":
            view_credentials(file_path)
        elif choice == "3":
            update_credential(file_path)
        elif choice == "4":
            delete_credential(file_path)
        elif choice == "5":
            print("Exiting the Credential Vault. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")