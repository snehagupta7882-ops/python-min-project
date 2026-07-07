def todo_list():
    task = []
    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            tasks = input("Enter the task: ")
            task.append(tasks)
        elif choice == 2:
            for i in task:
                print(i)
        elif choice == 3:
            tasks = input("Enter the task to remove: ")
            if tasks in task:
                task.remove(tasks)
            else:
                print("Task not found")
        
        elif choice == 4:
            print("Exit")
            break
        else:
            print("Invalid choice")
todo_list()
