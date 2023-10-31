class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.changes = []

    def add_money(self, amount):
        self.balance += amount
        self.changes.append(f"Added {amount}$ to the current balance at {datetime.datetime.now().strftime('%H:%M %d/%m/%Y')}")

    def subtract_money(self, amount):
        self.balance -= amount
        self.changes.append(f"Subtracted {amount}$ from the current balance at {datetime.datetime.now().strftime('%H:%M %d/%m/%Y')}")

    def view_balance(self):
        return self.balance

    def print_changes(self):
        for change in self.changes:
            print(change)


if __name__ == "__main__":
    bank_account = BankAccount(100)

    bank_account.add_money(50)
    bank_account.subtract_money(20)

    print(bank_account.view_balance())
    bank_account.print_changes()
