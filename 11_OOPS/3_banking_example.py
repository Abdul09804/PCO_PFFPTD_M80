class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.balance = amount
        self.transactions = [f"Account has been created with initial balance of Rs.{self.balance}"]

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Amount has Rs.{amount} has been credited by deposit. Total Balance is Rs.{self.balance}")
        else:
            raise ValueError ("Amount must be greater than 0")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError ("Insufficient Balance")
        self.balance -= amount
        self.transactions.append(f"Amount of Rs.{amount} has been debited by withdraw. Total Balance is Rs.{self.balance}")

    def statement(self):
        print(f"******************************Statement of {self.name}******************************")
        for item in self.transactions:
            print(item)
        print(f"**************************************END*******************************************")

    def check_balance(self):
        print(f"The total available balance is Rs.{self.balance}")

    def transfer(self, other, amount):
        if amount > self.balance:
            raise ValueError ("Insufficient Balance")
        self.balance -= amount
        other.balance += amount
        self.transactions.append(f"Amount of Rs.{amount} has been transferred to {other.name}'s Account. Total Balance is Rs.{self.balance}")
        other.transactions.append(f"Amount of Rs.{amount} has been credited by transfer from {self.name}'s account. Total Balance is {other.balance}")


p1 = BankAccount("John", 2000)
p2 = BankAccount("Mary", 5000)

print(p1.__dict__)
print(p2.__dict__)

# p1.deposit(-8000 )      # ValueError
p1.deposit(5000)
p2.deposit(10000)

p1.withdraw(4000)
# p2.withdraw(20000)      # ValueError: Insufficient Balance

p1.statement()
BankAccount.statement(p2)

# p1.check_balance()

p1.transfer(p2, 2000)
p2.statement()
p1.statement()





