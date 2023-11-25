class TaskNode:
    def __init__(self, task_id, priority, execution_time):
        self.task_id = task_id
        self.priority = priority
        self.execution_time = execution_time
        self.next = None

class TaskLinkedList:
    def __init__(self):
        self.head = None

    def add_task(self, task_id, priority, execution_time):
        new_task = TaskNode(task_id, priority, execution_time)
        if not self.head:
            self.head = new_task
            return
        # iterate to the last node
        last_task = self.head
        while last_task.next:
            last_task = last_task.next
        last_task.next = new_task

    def remove_task(self, task_id):
        current = self.head
        prev = None
        while current:
            if current.task_id == task_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
        print(f"Task with ID {task_id} not found.")

    def display_tasks(self):
        current = self.head
        while current:
            print(f"Task ID: {current.task_id}, Priority: {current.priority}, Execution Time: {current.execution_time}")
            current = current.next

class TaskStack:
    def __init__(self):
        self.items = []

    def push(self, task_id):
        self.items.append(task_id)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def display_high_priority_tasks(self):
        for task_id in reversed(self.items):
            print(f"High Priority Task ID: {task_id}")

class TaskQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, task_id):
        self.items.append(task_id)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def display_regular_priority_tasks(self):
        for task_id in self.items:
            print(f"Regular Priority Task ID: {task_id}")

class TaskSchedulingSystem:
    def __init__(self):
        self.task_list = TaskLinkedList()
        self.high_priority_tasks = TaskStack()
        self.regular_priority_tasks = TaskQueue()

    def add_task(self, task_id, priority, execution_time):
        self.task_list.add_task(task_id, priority, execution_time)
        if priority == 'high':
            self.high_priority_tasks.push(task_id)
            print(f"Task with ID {task_id} (High Priority) added.")
        else:
            self.regular_priority_tasks.enqueue(task_id)
            print(f"Task with ID {task_id} (Regular Priority) added.")

    def execute_task(self):
        if not self.high_priority_tasks.is_empty():
            task_id = self.high_priority_tasks.pop()
            print(f"Executing High Priority Task with ID: {task_id}")
            self.task_list.remove_task(task_id)
        elif not self.regular_priority_tasks.is_empty():
            task_id = self.regular_priority_tasks.dequeue()
            print(f"Executing Regular Priority Task with ID: {task_id}")
            self.task_list.remove_task(task_id)
        else:
            print("No tasks to execute.")

    def remove_task_by_id(self, task_id):
        self.task_list.remove_task(task_id)
        self.high_priority_tasks.items.remove(task_id) if task_id in self.high_priority_tasks.items else None
        self.regular_priority_tasks.items.remove(task_id) if task_id in self.regular_priority_tasks.items else None

    def display_tasks(self):
        print("\nAll Tasks:")
        self.task_list.display_tasks()
        print("\nHigh Priority Tasks:")
        self.high_priority_tasks.display_high_priority_tasks()
        print("\nRegular Priority Tasks:")
        self.regular_priority_tasks.display_regular_priority_tasks()

task_system = TaskSchedulingSystem()

while True:
    print("\nTask Scheduling System Menu:")
    print("1. Add Task")
    print("2. Execute Task")
    print("3. Remove Task by ID")
    print("4. Display Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task_id = input("Enter task ID: ")
        priority = input("Enter priority (high/regular): ")
        duration = int(input("Enter duration: "))
        task_system.add_task(task_id, priority, duration)
    elif choice == "2":
        task_system.execute_task()
    elif choice == "3":
        task_id = input("Enter task ID to remove: ")
        task_system.remove_task_by_id(task_id)
    elif choice == "4":
        task_system.display_tasks()
    elif choice == "5":
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-5).")

