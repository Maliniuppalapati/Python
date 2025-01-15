def main():
    tasks = []
    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Please enter your choice: ")

        if choice == '1':
            n_tasks = int(input("How many tasks you want to add? "))
            for i in range(n_tasks):
                task = input(f"Enter task {i + 1}: ")
                tasks.append({"task": task, "done": False})
            print("Tasks added successfully!")
        
        elif choice == '2':
            if tasks:
                print("\nYour Tasks:")
                for idx, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{idx + 1}. {task['task']} - {status}")
            else:
                print("No tasks to show. Add tasks first.")
        
        elif choice == '3':
            if tasks:
                task_index = int(input("Enter the task number to mark as done: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print(f"Task '{tasks[task_index]['task']}' marked as done!")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks available. Add tasks first.")
        
        elif choice == '4':
            print("Exiting the To-Do List. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
