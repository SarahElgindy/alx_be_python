class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount with an optional initial balance, default is 0.
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        :param amount: The amount to deposit (must be positive).
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if funds are sufficient.
        :param amount: The amount to withdraw (must be positive).
        :return: True if the withdrawal is successful, False if funds are insufficient.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        elif amount > self.__account_balance:
            print("Insufficient funds.")
            return False
        else:
            self.__account_balance -= amount
            return True

    def display_balance(self):
        """
        Display the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
