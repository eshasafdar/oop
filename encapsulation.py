# Encapsulation

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def get_balance(self):
        return self.balance

account = BankAccount()
account.deposit(100)
print(account.get_balance())
