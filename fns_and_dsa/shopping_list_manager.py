# Initialize an empty shopping list
shopping_list = []

# Function to display the menu
def display_menu():
    print("\nShopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the current list")
    print("4. Exit")

# Function to add an item to the shopping list
def add_item():
    item = input("Enter the item you want to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the list.")
    else:
        print("Item cannot be empty.")

# Function to remove an item from the shopping list
def remove_item():
    item = input("Enter the item you want to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' not found in the shopping list.")

# Function to view the current shopping list
def view_list():
    if shopping_list:
        print("\nCurrent Shopping List:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")
    else:
        print("Your shopping list is empty.")

# Main function to manage the shopping list
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            view_list()
        elif choice == "4":
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


