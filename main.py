from greetings import hello_english, hello_spanish, hello_french
from config import DEFAULT_LANGUAGE, SHOW_MENU


def get_greeting_function(language):
    """Return the appropriate greeting function based on language"""
    if language == "spanish":
        return hello_spanish
    elif language == "french":
        return hello_french
    else:  # default to english
        return hello_english


name = input("What's your name? ")

if SHOW_MENU:
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
        print("Invalid choice! Using default...")
        greeting_func = get_greeting_function(DEFAULT_LANGUAGE)
        print(greeting_func(name))
else:
    # Use default language from config
    greeting_func = get_greeting_function(DEFAULT_LANGUAGE)
    print(greeting_func(name))