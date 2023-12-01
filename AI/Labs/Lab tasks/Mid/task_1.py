class Passenger:
    def __init__(self,passenger_id,passenger_name) -> None:
        self.passenger_id=passenger_id
        self.passenger_name=passenger_name
    def __str__(self) -> str:
        return f"Passenger ID: {self.passenger_id}, Passenger Name: {self.passenger_name}"

class TrainReservationSystem:
    def __init__(self) -> None:
        self.passenger_list=LinkedList()
        self.waiting_list=Stack()
        self.confirmed_bookings=Queue()
        self.seats=10
    def book_ticket(self,passenger):
        if self.seats>0:
            self.passenger_list.append(passenger)
            self.confirmed_bookings.enqueue(passenger)
            self.seats-=1
        else:
            self.waiting_list.push(passenger)
    def cancel_ticket(self,passenger):
        if self.confirmed_bookings.contains(passenger):
            self.confirmed_bookings.remove(passenger)
            self.seats+=1
        elif self.waiting_list.contains(passenger):
            self.waiting_list.remove(passenger)
    def display_passengers(self):
        self.passenger_list.display()
        self.waiting_list.display()
        self.confirmed_bookings.display()

class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
    def __str__(self) -> str:
        return f"{self.data}"

class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def append(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=Node(data)
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current=self.head
            while current is not None:
                print(current.data)
                current=current.next
    def contains(self,data):
        if self.head is None:
            return False
        else:
            current=self.head
            while current is not None:
                if current.data==data:
                    return True
                current=current.next
            return False
    def remove(self,data):
        if self.head is None:
            return False
        else:
            current=self.head
            previous=None
            while current is not None:
                if current.data==data:
                    if previous is None:
                        self.head=current.next
                    else:
                        previous.next=current.next
                    return True
                previous=current
                current=current.next
            return False
        
class Stack:
    def __init__(self) -> None:
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def is_empty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def display(self):
        print(self.items)
    def contains(self,passenger):
        if(passenger in self.items):
            return True
        else:
            return False
    def remove(self,passenger):
        if(passenger in self.items):
            self.items.remove(passenger)
    
class Queue:
    def __init__(self) -> None:
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def is_empty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def display(self):
        print(self.items)
    def contains(self,passenger):
        if(passenger in self.items):
            return True
        else:
            return False
    def remove(self,passenger):
        if(passenger in self.items):
            self.items.remove(passenger)

trs=TrainReservationSystem()

while True:
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Display Passengers")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        passenger_id=int(input("Enter Passenger ID: "))
        passenger_name=input("Enter Passenger Name: ")
        passenger=Passenger(passenger_id,passenger_name)
        trs.book_ticket(passenger)
    elif choice==2:
        passenger_id=int(input("Enter Passenger ID: "))
        passenger_name=input("Enter Passenger Name: ")
        passenger=Passenger(passenger_id,passenger_name)
        trs.cancel_ticket(passenger)
    elif choice==3:
        trs.display_passengers()
    elif choice==4:
        break
    else:
        print("Invalid Choice")