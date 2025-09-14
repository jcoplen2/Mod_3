import hashlib

choice = input("Enter s for sting and f for file: ")

if choice == "s":
    text = input("enter text: ")
    print(hashlib.sha256(text.encode()).hexdigest())

elif choice == "f":
    filename = input("enter file path: ")
    with open(filename, "rb") as f:
        print(hashlib.sha256(f.read()).hexdigest)