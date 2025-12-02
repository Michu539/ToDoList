import tasks
from categories import Categories, Category
import datetime

def main():
    global task
    tasklist = tasks.TaskList()
    tl_categories = Categories()
    # UI
    while True:
        print("\n\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Edit Tasks")
        print("4. Categories related actions")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if not choice.isdigit():
            print("\nInvalid input. Enter a number!\n")
            continue

        if choice == '1':
            tasklist.add_task(tl_categories)

        elif choice == '2':
            tasklist.show_tasks()

        elif choice == '3':
            if not tasklist.tasks:
                print("No tasks to edit!")
                continue

            while True:
                print("\n\n=== Which task do you want to edit? ===")
                for number, task in enumerate(tasklist.tasks, start=1):
                    print(f"{number}. {task.name}")

                edit_choice = input('\nEnter task number (or "exit" to exit editing): ')

                if edit_choice == 'exit':
                    break

                if not edit_choice.isdigit():
                    print("\nInvalid input. Enter a number!\n")
                    continue

                if int(edit_choice) > len(tasklist.tasks):
                    print("\nInvalid input. No such task!\n")
                    continue

                task_to_edit = tasklist.tasks[int(edit_choice) - 1]
                while True:
                    print("\n\n== What do you want to edit? ==")
                    print("1. Name")
                    print("2. Category")
                    print("3. Importance")
                    print("4. Completion")
                    print("5. Delete This Task")
                    print("6. Exit")

                    edit_type_choice = input('\nEnter your choice: ')

                    if not edit_type_choice.isdigit():
                        print("\nInvalid input. Enter a number!\n")
                        continue

                    if edit_type_choice == '1':
                        task_to_edit.change_name()
                        break

                    elif edit_type_choice == '2':
                        if not tl_categories.categories:
                            print("\nNo categories exist! Add one first.")
                        else:
                            task_to_edit.change_category(tl_categories.categories)
                        break

                    elif edit_type_choice == '3':
                            task_to_edit.change_importance()
                            break

                    elif edit_type_choice == '4':
                        task_to_edit.change_completion()
                        break

                    elif edit_type_choice == '5':
                        delete_choice = input("\nAre you sure  you want to delete this task? (Y/N): ")
                        if delete_choice.upper() == 'Y':
                            tasklist.tasks.pop(int(edit_choice) - 1)
                            print("Task deleted!")
                        elif delete_choice.upper() == 'N':
                            print("Task won't be deleted!")
                            pass
                        else:
                            print("\nInvalid input. Please try again.\n")
                        break

                    elif edit_type_choice == '6':
                        break

                break

        elif choice == '4':
            print("\n\n=== What categories related actions do you want to do? ===")
            print("1. Add Category")
            print("2. Show Categories")
            print("3. Edit Category")
            print("4. Delete Category")
            print("5. Exit")

            choice = input("\nEnter your choice: ")

            while True:
                if not choice.isdigit():
                    print("\nInvalid input. Enter a number!\n")
                    continue

                if choice == '1':
                    tl_categories.add_category()
                    break

                if choice == '2':
                    tl_categories.show_categories()
                    break

                if choice == '3':
                    print("\n\n=== Which category do you want to edit? ===")
                    tl_categories.categories.enum_categories()

                    edit_choice = input('\nEnter category number (or "exit" to exit editing): ')

                    if str(edit_choice) == 'exit':
                        break

                    if not edit_choice.isdigit():
                        print("\nInvalid input. Enter a number!\n")
                        continue

                    if int(edit_choice) > len(tl_categories.categories):
                        print("\nInvalid input. No such task!\n")
                        continue

                    category_to_edit = tl_categories.categories[int(edit_choice) - 1]
                    category_to_edit.change_name()
                    break

                elif choice == '4':
                    print("\n\n=== Which category do you want to edit? ===")
                    tl_categories.categories.enum_categories()

                    edit_choice = input('\nEnter category number (or "exit" to exit editing): ')

                    if str(edit_choice) == 'exit':
                        break

                    if not edit_choice.isdigit():
                        print("\nInvalid input. Enter a number!\n")
                        continue

                    if int(edit_choice) > len(tl_categories.categories):
                        print("\nInvalid input. No such task!\n")
                        continue

                    else:
                        delete_choice = input("\nAre you sure  you want to delete this category? (Y/N): ")
                        if delete_choice.upper() == 'Y':
                            tl_categories.categories.pop(int(edit_choice) - 1)
                            print("Task deleted!")
                        elif delete_choice.upper() == 'N':
                            print("Task won't be deleted!")
                            pass
                        else:
                            print("\nInvalid input. Please try again.\n")
                        break

                elif choice == '5':
                    break

        elif choice == '5':
            break

        # admin action automatically adds 6 tasks and 2 categories for testing
        elif choice == '6':
            password = input("\nEnter password: ")
            if password == 'admin539':
                category1 = Category('Work')
                category2 = Category('School')
                tl_categories.categories.append(category1)
                tl_categories.categories.append(category2)
                task1 = tasks.Task('Task1', 'HIGH', datetime.date.today(), category1)
                task2 = tasks.Task('Task2', 'MEDIUM', datetime.date.today(), category1)
                task3 = tasks.Task('Task3', 'LOW', datetime.date.today(), category1)
                task4 = tasks.Task('Task4', 'HIGH', datetime.date.today(), category2)
                task5 = tasks.Task('Task5', 'MEDIUM', datetime.date.today(), category2)
                task6 = tasks.Task('Task6', 'LOW', datetime.date.today(), category2)
                admin_tasks = [task1, task2, task3, task4, task5, task6]
                for task in admin_tasks:
                    tasklist.tasks.append(task)
            else:
                print("\nInvalid password. You're not an admin!\n")


        else:
            print("\nInvalid input. Try again!\n")


if __name__ == "__main__":
    main()