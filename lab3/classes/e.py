class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, money):
        self.balance += money
        return self.balance
    def withdraw(self, money):
        if self.balance > money:
            self.balance -= money
            return f'YOUR BALANCE: {self.balance}'
        return "You can't do it!"
        

a1 = Account(input(), int(input()))
print("YOUR BALANCE:", a1.deposit(int(input())))
print(a1.withdraw(int(input())))