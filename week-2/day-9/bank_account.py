# python program to simulate a simple bank account system with deposit and withdrawal functionalities.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance # private attribute by convention

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
    
    @property
    def balance(self): # read-only public access to balance
        return self._balance
    
    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self._balance})"
    
acc = BankAccount("Alice", 100)
print(acc)  # BankAccount(owner='Alice', balance=100)
acc.deposit(50)
print(f"Balance after deposit: {acc.balance}")  # 150
acc.withdraw(30)
print(f"Balance after withdrawal: {acc.balance}")  # 120
# acc.withdraw(200)  # Raises ValueError: Insufficient funds.
# acc.deposit(-20)  # Raises ValueError: Deposit amount must be positive.
