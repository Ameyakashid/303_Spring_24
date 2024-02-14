import string
from datetime import date

def encode(text, shift):
    result = ""
    lo_text=text.lower()
    for char in lo_text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char) + shift_amount
            if char.islower():
                char_code -= 26 if char_code > ord('z') else 0
            else:
                char_code -= 26 if char_code > ord('Z') else 0
            result += chr(char_code)
        else:
            result += char
    return list(string.ascii_lowercase),result





 

def decode(input_text, shift):
    return encode(input_text, -shift)[1]

class BankAccount:
    def __init__(self, name="Rainy", ID="1234", creation_date=date.today(), balance=0):
        if creation_date > date.today():
            raise Exception("Creation date cannot be in the future.")
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Cannot deposit a negative amount.")
            return self.view_balance()
        self.balance += amount
        return self.view_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print("Cannot withdraw a negative amount.")
            return self.view_balance()
        self.balance -= amount
        return self.view_balance()

    def view_balance(self):
        return f"Current balance: ${self.balance}"

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if (date.today() - self.creation_date).days < 180:
            print("Withdrawals are only permitted after 180 days of account creation.")
            return super().view_balance()
        if self.balance - amount < 0:
            print("Overdrafts are not permitted.")
            return super().view_balance()
        return super().withdraw(amount)

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= 30  # Overdraft fee
        return super().withdraw(amount)


