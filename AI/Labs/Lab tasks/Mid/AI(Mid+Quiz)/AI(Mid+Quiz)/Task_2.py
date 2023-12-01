class Task:
    def __init__(self, task_id, priority, execution_time):
        self.task_id = task_id
        self.priority = priority
        self.execution_time = execution_time
class Node:
    def __init__(self, task):
        self.task = task
        self.next = None
class TaskScheduler:
    def __init__(self):
        self.task_list = None
        self.high_priority_stack = []
        self.regular_priority_queue = []
    def add_task(self, task):
        new_node = Node(task)
        new_node.next = self.task_list
        self.task_list = new_node
        if task.priority == 'high':
            self.high_priority_stack.append(task)
            print(f"\nHigh-priority task {task.task_id} added.")
        else:
            self.regular_priority_queue.append(task)
            print(f"\nRegular-priority task {task.task_id} added to the queue.")
    def execute_task(self):
        if self.high_priority_stack:
            task = self.high_priority_stack.pop()
            print(f"\nExecuting high-priority task {task.task_id} with execution time {task.execution_time}.")
        elif self.regular_priority_queue:
            task = self.regular_priority_queue.pop(0)
            print(f"\nExecuting regular-priority task {task.task_id} with execution time {task.execution_time}.")
        else:
            print("\nNo tasks available to execute.")
    def remove_task(self, task_id):
        current_task = self.task_list
        prev_task = None
        while current_task:
            if current_task.task.task_id == task_id:
                if current_task.task.priority == 'high':
                    self.high_priority_stack.remove(current_task.task)
                    print(f"\nHigh-priority task {task_id} removed.")
                else:
                    self.regular_priority_queue.remove(current_task.task)
                    print(f"\nRegular-priority task {task_id} removed.")
                if prev_task:
                    prev_task.next = current_task.next
                else:
                    self.task_list = current_task.next
                return
            prev_task = current_task
            current_task = current_task.next
        print(f"\nTask with ID {task_id} not found.")
    def display_tasks(self):
        print("\nTask List:")
        current_task = self.task_list
        while current_task:
            task = current_task.task
            print(f"Task ID: {task.task_id}, Priority: {task.priority}, Execution Time: {task.execution_time}")
            current_task = current_task.next
def display_menu():
    print("1. Add Task")
    print("2. Execute Task")
    print("3. Remove Task")
    print("4. Display Tasks")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice
# Example usage with user input and menu:
task_scheduler = TaskScheduler()

while True:
    Choice = display_menu()

    if Choice == '1':
        task_id = int(input("Enter Task ID: "))
        priority = input("Enter Priority ('high' or 'regular'): ")
        execution_time = int(input("Enter Execution Time: "))
        task = Task(task_id, priority, execution_time)
        task_scheduler.add_task(task)
    elif Choice == '2':
        task_scheduler.execute_task()
    elif Choice == '3':
        task_id = int(input("Enter Task ID to remove: "))
        task_scheduler.remove_task(task_id)
    elif Choice == '4':
        task_scheduler.display_tasks()
    elif Choice == '5':
        print("Exited")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
