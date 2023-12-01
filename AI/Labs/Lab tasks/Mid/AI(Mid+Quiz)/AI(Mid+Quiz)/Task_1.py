class Node:
    def __init__(self, passenger):
        self.passenger = passenger
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_passenger(self, passenger):
        passenger = Node(passenger)
        passenger.next = self.head
        self.head = passenger
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
class TrainReservationSystem:
    def __init__(self, max_seats):
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
