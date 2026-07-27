queue = []
MAX = 5

def enqueue():
    if len(queue) == MAX:
        print("Parking is Full!")
    else:
        car = input("Enter Car Number: ")
        queue.append(car)
        print(car, "has entered the parking.")

def dequeue():
    if len(queue) == 0:
        print("Parking is Empty!")
    else:
        car = queue.pop(0)
        print(car, "has exited the parking.")

def display():
    if len(queue) == 0:
        print("No cars in the parking.")
    else:
        print("Cars in Parking:")
        for car in queue:
            print(car)

while True:
    print("\n--- Car Parking System ---")
    print("1. Park Car (Enqueue)")
    print("2. Remove Car (Dequeue)")
    print("3. Display Cars")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting Program...")
        break
    else:
        print("Invalid choice!")



       
