shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list= []

    while True:
        display_menu()
        choice = input("choose an option(1-4):")

        if choice == "1":
            item = input("Enter the item to add:")
            if item:
                shopping_list.append(item)
                print(f"{item} has been added.")
            else:
                print("Enter a valid item")

        elif choice == "2":
            item = input("Enter the item you want to remove:")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the list.")
            else:
                print(f"{item} not found, please enter a valid item.")

        elif choice == "3":
            if shopping_list:
                print("Current shopping list:")
                for idx, item in enumerate(shopping_list, start=1):
                  print(f"{idx}. {item}")
            else:
                print("Your shooping list is empty.")

        elif choice == "4":
            print("Exiting the shopping list manager, Goodbye")
            break
        else:
            print("Invalid choice. please enter a valid number")

if __name__ == "__main__":
    main()

