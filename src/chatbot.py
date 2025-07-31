"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "Anannya"
__version__ = "1.0"
__credits__ = "COMP-1327 Faculty"

ACCOUNTS = {
    123456: {
        "balance": 1000.0
    },
    789012: {
        "balance": 2000.0
    }
} 

VALID_TASKS = [
    "balance", 
    "deposit", 
    "exit"
]

def check_balance(account_number):
    """Display the balance for the given account."""
    try:
        balance = ACCOUNTS[account_number]["balance"]
        print(f"Your current balance is ${balance:.2f}")
    except KeyError:
        print("Error: Account not found.")

def make_deposit(account_number):
    """Prompt user to deposit amount and update the account balance."""
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        ACCOUNTS[account_number]["balance"] += amount
        print(f"${amount:.2f} deposited successfully.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def chatbot():
    """Performs the Chatbot functionality."""
    COMPANY_NAME = "PIXELL River Financial"
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! Let's get chatting!")

    # Ask for account number
    try:
        account_number = int(input("Please enter your 6-digit account number: "))
    except ValueError:
        print("Invalid input. Account number must be numbers only.")
        return

    if account_number not in ACCOUNTS:
        print("Account not found. Please try again.")
        return

    # Task loop
    while True:
        task = input("What would you like to do? (balance/deposit/exit): ").lower()

        if task == "balance":
            check_balance(account_number)
        elif task == "deposit":
            make_deposit(account_number)
        elif task == "exit":
            print(f"Thank you for banking with {COMPANY_NAME}.")
            break
        else:
            print("Invalid task. Please choose from balance, deposit, or exit.")

if __name__ == "__main__":
    chatbot()
