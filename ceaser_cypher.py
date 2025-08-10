

def encode(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            base_code = ord("A") if char.isupper() else ord("a")
            shifted = chr((ord(char) - base_code + key) % 26 + base_code)
            result += shifted
        else:
            result += char
    return result 

def decode(message, key):
    return encode(message, -key)

if __name__ == "__main__":
    choice = input("Enter encription/decription [enc/dec]: ")

    if choice == "enc":
        message = input("Enter your Message: ").strip()
        key = int(input("Enter the key/offset [1 - 26]: "))
        print(f"Encrypted str:\n{encode(message,key)}\n")
    elif choice == "dec":
        message = input("Enter your Message: ")
        key = int(input("Enter the key- offset: "))
        print(f"Decrypted str:\n{decode(message,key)}\n") 
    else:
        print("Invalid Choice")