stack = []

while True:
    print("\n--- Library Stack Operations ---")
    print("1. Push (Add Book)")
    print("2. Pop (Remove Book)")
    print("3. Display Stack")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book title: ")
        stack.append(book)
        print(book, "added to the stack.")

    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty. No book to remove.")
        else:
            book = stack.pop()
            print(book, "removed from the stack.")

    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Books in the stack:")
            for i in range(len(stack) - 1, -1, -1):
                print(stack[i])

    elif choice == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid choice.")
