# Imagine you are developing a task scheduling system for a computer. Each task has a priority 
# level and estimated execution time. Your goal is to use a combination of a linked list, a stack, 
# and a queue to manage the tasks efficiently.
# Here are the components:
# Linked List for Task List: Each task is represented by a node in a linked list. The linked list 
# maintains tasks in the order they are added.
# Stack for High Priority Tasks: A stack is used to store tasks with high priority. High-priority 
# tasks are pushed onto the stack for quick retrieval.
# Queue for Regular Priority Tasks: A queue is used to store tasks with regular priority.
# Regular priority tasks are enqueued at the end of the queue.
# Operations:
# Add Task:
# A new task is added to the linked list. If the task has high priority, it is also pushed onto the 
# stack. If the task has regular priority, it is enqueued at the end of the queue.
# Execute Task:
# The system executes tasks in the following order: Execute a high-priority task from the stack if 
# available. If the stack is empty, execute a regular-priority task from the front of the queue.
# Remove Task:
# A task can be removed from the system based on its ID.

# Task class
class Task:
    def __init__(self,task_id,task_priority,task_time) -> None:
        self.task_id=task_id
        self.task_priority=task_priority
        self.task_time=task_time
    def __str__(self) -> str:
        return f"Task ID: {self.task_id}, Task Priority: {self.task_priority}, Task Time: {self.task_time}"

# TaskScheduler class
class TaskScheduler:
    def __init__(self) -> None:
        self.task_list=LinkedList()
        self.high_priority_tasks=Stack()
        self.regular_priority_tasks=Queue()
    def add_task(self,task):
        self.task_list.append(task)
        if task.task_priority=="high":
            self.high_priority_tasks.push(task)
        elif task.task_priority=="regular":
            self.regular_priority_tasks.enqueue(task)
    def execute_task(self):
        if not self.high_priority_tasks.is_empty():
            self.high_priority_tasks.pop()
        elif not self.regular_priority_tasks.is_empty():
            self.regular_priority_tasks.dequeue()
    def remove_task(self,task):
        if self.task_list.contains(task):
            self.task_list.remove(task)
            if task.task_priority=="high":
                self.high_priority_tasks.remove(task)
            elif task.task_priority=="regular":
                self.regular_priority_tasks.remove(task)
    def display_tasks(self):
        self.task_list.display()
        self.high_priority_tasks.display()
        self.regular_priority_tasks.display()

# Node class
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
    def __str__(self) -> str:
        return f"{self.data}"

# LinkedList class
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
            print("List is empty")
        else:
            current=self.head
            previous=None
            while current is not None:
                if current.data==data:
                    if previous is None:
                        self.head=current.next
                    else:
                        previous.next=current.next
                    break
                previous=current
                current=current.next

# Stack class
class Stack:
    def __init__(self) -> None:
        self.top=None
    def push(self,data):
        if self.top is None:
            self.top=Node(data)
        else:
            new_node=Node(data)
            new_node.next=self.top
            self.top=new_node
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            self.top=self.top.next
    def is_empty(self):
        return self.top is None
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            current=self.top
            while current is not None:
                print(current.data)
                current=current.next

# Queue class
class Queue:
    def __init__(self) -> None:
        self.front=None
        self.rear=None
    def enqueue(self,data):
        if self.front is None:
            self.front=Node(data)
            self.rear=self.front
        else:
            new_node=Node(data)
            self.rear.next=new_node
            self.rear=new_node
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            self.front=self.front.next
    def is_empty(self):
        return self.front is None
    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            current=self.front
            while current is not None:
                print(current.data)
                current=current.next

# Test code
task_scheduler=TaskScheduler()

while True:
    print("1. Add Task")
    print("2. Execute Task")
    print("3. Remove Task")
    print("4. Display Tasks")
    print("5. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        task_id=int(input("Enter task ID: "))
        task_priority=input("Enter task priority (high/regular): ")
        task_time=int(input("Enter task time: "))
        task_scheduler.add_task(Task(task_id,task_priority,task_time))
    elif choice==2:
        task_scheduler.execute_task()
    elif choice==3:
        task_id=int(input("Enter task ID: "))
        task_priority=input("Enter task priority (high/regular): ")
        task_time=int(input("Enter task time: "))
        task_scheduler.remove_task(Task(task_id,task_priority,task_time))
    elif choice==4:
        task_scheduler.display_tasks()
    elif choice==5:
        break
    else:
        print("Invalid choice")
