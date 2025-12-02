import datetime
from random import choice

import categories
from categories import Categories, Category

class Task:
    def __init__(self, name, importance, date, category=None):
        self.name = name
        self.category = category
        self.importance = importance
        self.completion = "No"
        self.date = date


    # changes name of a task
    def change_name(self):
        self.name = input("\nEnter new task name: ")
        print(f'\nTask name changed to "{self.name}"')


    # changes completion of a task
    def change_completion(self):
        if self.completion == 'Yes':
            choice = input('\nDo you want to change this task completion to incomplete? (Y/N): ')
            if choice.upper() == 'Y':
                self.completion = 'No'
                print('\nThis task is now incomplete.')
            elif choice.upper() == 'N':
                pass
            else:
                print("\nInvalid input. Please try again.\n")
        elif self.completion == 'No':
            choice = input('\nDo you want to complete this task? (Y/N): ')
            if choice.upper() == 'Y':
                self.completion = 'Yes'
                print('\nThis task is now complete.')
            elif choice.upper() == 'N':
                pass
            else:
                print("\nInvalid input. Please try again.\n")


    # changes importance of a task
    def change_importance(self):
        while True:
            if self.importance == 'HIGH':
                while True:
                    importance = input("\nChange importance of this task (to MEDIUM or LOW): ")
                    if importance.upper() == 'MEDIUM':
                        self.importance = 'MEDIUM'
                        break
                    elif importance.upper() == 'LOW':
                        self.importance = 'LOW'
                        break
                    else:
                        print("\nInvalid input. Please try again.\n")
                break
            elif self.importance == 'MEDIUM':
                while True:
                    importance = input("\nChange importance of this task (to HIGH or LOW): ")
                    if importance.upper() == 'HIGH':
                        self.importance = 'HIGH'
                        break
                    elif importance.upper() == 'LOW':
                        self.importance = 'LOW'
                        break
                    else:
                        print("\nInvalid input. Please try again.\n")
                break
            elif self.importance == 'LOW':
                while True:
                    importance = input("\nChange importance of this task (to HIGH or MEDIUM): ")
                    if importance.upper() == 'MEDIUM':
                        self.importance = 'MEDIUM'
                        break
                    elif importance.upper() == 'HIGH':
                        self.importance = 'HIGH'
                        break
                    else:
                        print("\nInvalid input. Please try again.\n")
                break
        print(f'\nImportance of this task is now {self.importance}.')


    def change_category(self, categories_list):
        print('\nChoose a new category for this task:')
        for number, category in enumerate(categories_list, start=1):
            print(f'{number}. {category.name}')
        while True:
            choice = input('\nEnter category number: ')
            if not choice.isdigit():
                print("\nInvalid input. Please try again!\n")
                continue
            elif int(choice) > len(categories_list):
                print("\nInvalid input. No such category!\n")
                continue
            else:
                self.category = categories_list[int(choice) - 1]
                print(f'\nTask category changed to "{self.category.name}"')
                break



class TaskList:
    def __init__(self):
        # raw list of the tasks
        self.tasks = []

    # adds task to self.tasks using user inputs
    def add_task(self, tl_categories=None):
        name = input("\nEnter task name: ")

        category = None
        if tl_categories and tl_categories.categories:
            print("\nTo which category do you want this task to belong?")
            for number, cat in enumerate(tl_categories.categories, start=1):
                print(f"{number}. {cat.name}")
            print('0. No category')
            while True:
                cat_choice = input("Enter category number: ")
                if not cat_choice.isdigit():
                    print("\nInvalid input. Please try a number!\n")
                if cat_choice == '0':
                    category = None
                elif int(cat_choice) > len(tl_categories.categories):
                        print("\nInvalid input. No such category!\n")
                        continue
                else:
                    category = tl_categories.categories[int(cat_choice) - 1].name
                    break
        else:
            print('\nThere are no created categories to associate this task with.')

        while True:
            importance = input("\nChoose importance of this task (HIGH, MEDIUM or LOW): ")
            if importance.upper() == 'HIGH':
                importance = 'HIGH'
                break
            elif importance.upper() == 'MEDIUM':
                importance = 'MEDIUM'
                break
            elif importance.upper() == 'LOW':
                importance = 'LOW'
                break
            else:
                print("\nInvalid input. Please try again.\n")

        date = datetime.date.today()

        new_task = Task(name, importance, date, category)
        self.tasks.append(new_task)
        print(
            f"\nNew task has been added:\n"
            f'\nName: {name}\n'
            f'Category: {category if category else None}\n'
            f'Creation date (YYYY:MM:DD): {date}\n'
            f'Importance: {importance}\n'
            f'Completed: No\n'
        )


    # prints all tasks in user view
    def show_tasks(self):
        if len(self.tasks) == 0:
            print("\nNo tasks have been added.\n")
        else:
            while True:
                print("\n\n=== How do you want your tasks to be shown? ===")
                print("1. Alphabetically")
                print("2. By Category")
                print("3. By Importance")
                print("4. By Completion")
                print("5. Exit")

                choice = input('\nEnter your choice: ')

                if not choice.isdigit():
                    print("\nInvalid input. Enter a number!\n")

                # sorted alphabetically
                if choice == '1':
                    print("\n=== Your Tasks: ===")
                    # sort tasks alphabetically
                    sorted_tasks = sorted(self.tasks, key=lambda task: task.name.lower())
                    # print each group
                    for task in sorted_tasks:
                        print(
                            f'\nName: {task.name}\n'
                            f'Category: {task.category.name}\n'
                            f'Creation date (YYYY:MM:DD): {task.date}\n'
                            f'Importance: {task.importance}\n'
                            f'Completed: {task.completion}\n'
                        )
                    break

                # sorted by category
                elif choice == '2':
                    print("\n=== Your Tasks (By Category): ===")
                    # group tasks by category
                    grouped = {}
                    for task in self.tasks:
                        cat = task.category.name
                        grouped.setdefault(cat, []).append(task)
                    # print each category group
                    for cat, tasks in sorted(grouped.items()):
                        print(f"\n= {cat.upper()}: =")
                        for task in tasks:
                            print(f'\nName: {task.name}\n'
                                  f'Creation date (YYYY:MM:DD): {task.date}\n'
                                  f'Importance: {task.importance}\n'
                                  f'Completed: {task.completion}\n')
                    break

                # sorted by importance
                elif choice == '3':
                    print("\n=== Your Tasks (By Importance): ===")
                    # group by importance
                    order = ['HIGH', 'MEDIUM', 'LOW']
                    grouped = {level: [] for level in order}
                    for task in self.tasks:
                        grouped[task.importance].append(task)
                    # print each importance group
                    for importance in order:
                        if grouped[importance]:
                            print(f"\n= {importance.upper()}: =")
                        for task in grouped[importance]:
                            print(f'\nName: {task.name}\n'
                                  f'Category: {task.category.name}\n'
                                  f'Creation date (YYYY:MM:DD): {task.date}\n'
                                  f'Completed: {task.completion}\n')
                    break

                # sorted by completion
                elif choice == '4':
                    print("\n=== Your Tasks (By Completion): ===")
                    # group by completion
                    grouped = {'Yes': [], 'No': []}
                    for task in self.tasks:
                        grouped[task.completion].append(task)
                    # print each completion group
                    for completion in ['Yes', 'No']:
                        label = 'COMPLETED' if completion == 'Yes' else 'NOT COMPLETED'
                        if grouped[completion]:
                            print(f'\n= {label} =')
                        for task in grouped[completion]:
                            print(f'\nName: {task.name}\n'
                                  f'Category: {task.category.name}\n'
                                  f'Creation date (YYYY:MM:DD): {task.date}\n'
                                  f'Importance: {task.importance}\n')
                    break

                # exit
                elif choice == '5':
                    break

                else:
                    print("\nInvalid input. Please try again!\n")