def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        # Check if the input is a digit and within the valid range
        if choice.isdigit() and 1 <= int(choice) <= 4:
            choice = int(choice)
            
            if choice == 1:
                item = input("Enter the item to add: ")
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            elif choice == 2:
                item = input("Enter the item to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from your shopping list.")
                else:
                    print(f"'{item}' not found in your shopping list.")
            elif choice == 3:
                if shopping_list:
                    print("\nYour shopping list:")
                    for i, item in enumerate(shopping_list, 1):
                        print(f"{i}. {item}")
                else:
                    print("Your shopping list is empty.")
            elif choice == 4:
                print("Goodbye!")
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()