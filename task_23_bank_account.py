class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance = self.balance - amount
            print(f"Withdrawn: {amount}")

    def show_balance(self):
        print(f"Current balance: {self.balance}")


account = BankAccount("Anusha", 1000)

print(f"Account owner: {account.owner}")
account.show_balance()

account.deposit(500)
account.show_balance()

account.withdraw(300)
account.show_balance()

account.withdraw(5000)
account.show_balance()