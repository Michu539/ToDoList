class Category:
    def __init__(self, name):
        self.name = name


    def change_name(self):
        self.name = input("\nEnter new category name: ")
        print(f'\nTask name changed to "{self.name}"')


class Categories:
    def __init__(self):
        self.categories = []

    def add_category(self):
        name = input("\nEnter category name: ")

        new_category = Category(name)
        self.categories.append(new_category)
        print(
            f"\nNew category has been added:\n"
            f'\nName: {name}\n'
        )


    def show_categories(self):
        if len(self.categories) == 0:
            print("\nNo categories have been added.\n")
        else:
            print("\n=== Your Categories: ===\n")
            for category in self.categories:
                print(
                    f'{category.name}'
                )


    def enum_categories(self):
        for number, category in enumerate(self.categories, start=1):
            print(f"{number}. {category.name}")