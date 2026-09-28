def main():
    greeting = input("Greeting: ")
    f_greeting = greeting.lower().strip()

    if f_greeting.startswith("hello"):
        print("$0")
    elif f_greeting.startswith("h") and not(f_greeting.startswith("hello")):
        print("$20")
    else:
        print("$100")

main()


