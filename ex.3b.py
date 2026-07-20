class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(value, "pushed into stack")

    def pop(self):
        if self.top is None:
            print("Stack is Empty!")
            return

        temp = self.top
        self.top = self.top.next
        print(temp.data, "popped from stack")

    def display(self):
        if self.top is None:
            print("Stack is Empty!")
            return

        temp = self.top
        print("Stack Elements:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")


stack = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        stack.push(value)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.display()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice!")
