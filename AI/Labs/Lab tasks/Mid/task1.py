# class Passenger:
#     def __init__(self, name):
#         self.name = name
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, name):
#         new_node = Passenger(name)
#         if not self.head:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def display_passengers(self):
#         current = self.head
#         while current:
#             print(current.name)
#             current = current.next

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()

#     def is_empty(self):
#         return len(self.items) == 0

#     def display_waiting_list(self):
#         for passenger in reversed(self.items):
#             print(passenger)

# class Queue:
#     def __init__(self):
#         self.items = []

#     def enqueue(self, item):
#         self.items.append(item)

#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)

#     def is_empty(self):
#         return len(self.items) == 0

#     def display_confirmed_bookings(self):
#         for passenger in self.items:
#             print(passenger)

# class TrainReservationSystem:
#     def __init__(self,total_seats):
#         self.passenger_list = LinkedList()
#         self.waiting_list = Stack()
#         self.confirmed_bookings = Queue()
#         self.total_seats = total_seats

#     def book_ticket(self, passenger_name):
#         self.passenger_list.append(passenger_name)
#         if self.total_seats > 0:
#             self.confirmed_bookings.enqueue(passenger_name)
#             print(f"Seat Successfully booked for {passenger_name}.")
#             self.total_seats -= 1
#         else:
#             self.waiting_list.push(passenger_name)
#             print(f"Train fully booked. {passenger_name} added to the waiting list.")

#     def cancel_booking(self, passenger_name):
#         if passenger_name in self.confirmed_bookings.items:
#             self.confirmed_bookings.items.remove(passenger_name)
#             self.total_seats += 1
#             print(f"{passenger_name}'s booking has been canceled.")
#             if not self.waiting_list.is_empty():
#                 passenger_from_waiting = self.waiting_list.pop()
#                 self.confirmed_bookings.enqueue(passenger_from_waiting)
#                 self.total_seats -= 1
#                 print(f"Seat successfully booked for {passenger_from_waiting} from the waiting list.")
#         elif passenger_name in self.waiting_list.items:
#             self.waiting_list.items.remove(passenger_name)
#             print(f"{passenger_name}'s waiting list entry has been removed.")
#         else:
#             print(f"{passenger_name} not found in bookings or waiting list.")

#     def display_passengers(self):
#         print("\nPassengers with confirmed bookings:")
#         self.confirmed_bookings.display_confirmed_bookings()
#         print("\nPassengers on the waiting list:")
#         self.waiting_list.display_waiting_list()
#         print("\nAll Passengers:")
#         self.passenger_list.display_passengers()


# max_seats = 3
# train_system = TrainReservationSystem(max_seats)

# while True:
#     print("\nTrain Reservation System Menu:")
#     print("1. Book Ticket")
#     print("2. Cancel Booking")
#     print("3. Display Passengers")
#     print("4. Exit")

#     choice = input("Enter your choice (1-4): ")

#     if choice == "1":
#         name = input("Enter passenger name: ")
#         train_system.book_ticket(name)
#     elif choice == "2":
#         name = input("Enter passenger name to cancel booking: ")
#         train_system.cancel_booking(name)
#     elif choice == "3":
#         train_system.display_passengers()
#     elif choice == "4":
#         print("Exiting the program. Thank you!")
#         break
#     else:
#         print("Invalid choice. Please enter a valid option (1-4).")


class Node:
    def _init_(self, passenger):
        self.passenger = passenger
        self.next = None
class LinkedList:
    def _init_(self):
        self.head = None
    def add_passenger(self, passenger):
        passenger = Node(passenger)
        passenger.next = self.head
        self.head = passenger
class Stack:
    def _init_(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
class Queue:
    def _init_(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
class TrainReservationSystem:
    def _init_(self, max_seats):
        self.passengerList = LinkedList()
        self.waiting_list = Stack()
        self.confirmed_bookings = Queue()
        self.max_seats = max_seats
    def book_ticket(self, passenger_name):
        if self.max_seats > 0:
            self.passengerList.add_passenger(passenger_name)
            self.confirmed_bookings.enqueue(passenger_name)
            self.max_seats -= 1
            print(f"\n{passenger_name} has a confirmed booking.")
        else:
            self.waiting_list.push(passenger_name)
            print(f"\nTrain is fully booked. {passenger_name} added to the waiting list.")
    def cancel_booking(self, passenger):
        if passenger in self.confirmed_bookings.items:
            self.confirmed_bookings.items.remove(passenger)
            self.max_seats += 1
            print(f"\n{passenger}'s booking has been canceled.")
        elif passenger in self.waiting_list.items:
            self.waiting_list.items.remove(passenger)
            print(f"\n{passenger}'s waiting list entry has been canceled.")
        else:
            print(f"\n{passenger} not found in bookings or waiting list.")
    def display_passengers(self):
        print("\nPassenger List:")
        current_passenger = self.passengerList.head
        while current_passenger:
            print(current_passenger.passenger)
            current_passenger = current_passenger.next
        print("\nConfirmed Bookings:")
        for passenger in self.confirmed_bookings.items:
            print(passenger)
        print("\nWaiting List:")
        for passenger in self.waiting_list.items:
            print(passenger)
def Menu():
    print("\nTrain Reservation System Menu:")
    print("1. Book Ticket")
    print("2. Cancel Booking")
    print("3. Display Passengers")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    return choice
max_seats = int(input("Enter number of seats:"))
train_system = TrainReservationSystem(max_seats)
while True:
    Choice = Menu()
    if Choice == '1':
        passenger_name = input("Enter passenger name: ")
        train_system.book_ticket(passenger_name)
    elif Choice == '2':
        passenger_name = input("Enter passenger name to cancel booking: ")
        train_system.cancel_booking(passenger_name)
    elif Choice == '3':
        train_system.display_passengers()
    elif Choice == '4':
        print("Exited")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")