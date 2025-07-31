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

def chatbot():
    """Performs the Chatbot functionality."""
    COMPANY_NAME = "PiXELL River Financial"

def check_balance(account_number):
     #Display the balance for the give account.
     try:
         balance = ACCOUNTS[account_number]["balance"]
         print(f"Your current balance is ${"balance"}")
     except KeyError:
        print("Error: Account not found.")
#add make_deposit()
def make_deposit (account_number):

     try:
        amount = float(input("enter the amount to deposite: "))
     except ValueError:
        print("Invalid amount.please enter a number.")
        return
        ACCOUNTS[account_number]["balance"] += amount
        print(f"${amount:.2f} deposited successfully.")



    # Print welcome message
        print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")
    
     try:
        account_number = int(input("Please enter your 6-digit account number: "))
     except ValueError:
        print("Invalid input. Account number must be numbers only.")
        return
    
if account_number not in ACCOUNTS:
     print("Account not found. please try again ")

    # Print thank you message
     print(f"Thank you for banking with {COMPANY_NAME}.")

if __name__ == "__main__":
    chatbot()
