from greetings import hello_english, hello_spanish, hello_french

name = input("What's your name? ")

print("Choose a language:")
print("1. English")
print("2. Spanish")
print("3. French")

choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    print(hello_english(name))
elif choice == "2":
    print(hello_spanish(name))
elif choice == "3":
    print(hello_french(name))
else:
    print("Invalid choice!")