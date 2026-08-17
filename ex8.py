class Node:
    def __init__(self, name, time, purpose):
        self.name = name
        self.time = time
        self.purpose = purpose
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, name, time, purpose):
        new = Node(name, time, purpose)

        if self.root is None:
            self.root = new
            return

        current = self.root

        while True:
            if name < current.name:
                if current.left is None:
                    current.left = new
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new
                    return
                current = current.right

    def search_name(self, name):
        current = self.root

        while current:
            if name == current.name:
                return current
            elif name < current.name:
                current = current.left
            else:
                current = current.right

        return None

    def search_time(self, node, time):
        if node is None:
            return None

        if node.time == time:
            return node

        result = self.search_time(node.left, time)

        if result:
            return result

        return self.search_time(node.right, time)

    def minimum(self, node):
        current = node

        while current.left:
            current = current.left

        return current

    def delete(self, node, name):
        if node is None:
            return None

        if name < node.name:
            node.left = self.delete(node.left, name)

        elif name > node.name:
            node.right = self.delete(node.right, name)

        else:
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            temp = self.minimum(node.right)

            node.name = temp.name
            node.time = temp.time
            node.purpose = temp.purpose

            node.right = self.delete(node.right, temp.name)

        return node

    def sort_by_name(self, node):
        if node:
            self.sort_by_name(node.left)
            print("Name:", node.name)
            print("Time:", node.time)
            print("Purpose:", node.purpose)
            print()
            self.sort_by_name(node.right)


bst = BST()

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Search by Visitor Name")
    print("4. Search by Entry Time")
    print("5. Sort by Visitor Name")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter visitor name: ")
        time = input("Enter entry time: ")
        purpose = input("Enter purpose: ")

        bst.insert(name, time, purpose)

        print("Entry inserted")

    elif choice == 2:
        name = input("Enter visitor name: ")

        if bst.search_name(name):
            bst.root = bst.delete(bst.root, name)
            print("Entry deleted")
        else:
            print("Entry not found")

    elif choice == 3:
        name = input("Enter visitor name: ")

        result = bst.search_name(name)

        if result:
            print("Name:", result.name)
            print("Time:", result.time)
            print("Purpose:", result.purpose)
        else:
            print("Entry not found")

    elif choice == 4:
        time = input("Enter entry time: ")

        result = bst.search_time(bst.root, time)

        if result:
            print("Name:", result.name)
            print("Time:", result.time)
            print("Purpose:", result.purpose)
        else:
            print("Entry not found")

    elif choice == 5:
        if bst.root is None:
            print("No entries found")
        else:
            print("\nVisitors sorted by name:")
            bst.sort_by_name(bst.root)

    elif choice == 6:
        break

    else:
        print("Invalid choice")
