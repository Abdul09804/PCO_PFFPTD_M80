class BankAccount:
    interest_rate = 4.0

    def __init__(self, fname, lname, amount):
        self.fname = fname
        self.lname = lname
        self.balance = amount
        self.transactions = [f"Account has been created with initial deposit of Rs.{self.balance}"]

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Amount of Rs.{amount} has been credited by deposit, Total Balance is Rs.{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Amount of Rs.{amount} has been debited by withdraw, Total Balance is Rs.{self.balance}")
        else:
            raise ValueError

    def statement(self):
        print('*' * 100)
        for line in self.transactions:
            print(line)
        print('*' * 100)

    def roi(self):
        interest_amount = self.balance * (self.interest_rate/100)
        self.balance += interest_amount
        self.transactions.append(f"Amount of Rs.{interest_amount} has been credited by interest. Total Balance is Rs.{self.balance}")


class SavingsBankAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 10000:
            raise ValueError ("Can not withdraw more than Rs.10000 at once")
        super().withdraw(amount)


# cust1 = SavingsBankAccount("Mary", "Joseph", 2000)
# cust1.deposit(10000)
# cust1.statement()
# cust1.roi()
# cust1.statement()
# # cust1.withdraw(11000)       # ValueError: Can not withdraw more than Rs.10000 at once
# cust1.withdraw(5000)
# cust1.statement()


class SeniorCitizenAccount(BankAccount):
    interest_rate = 5.0
    def __init__(self, fname, lname, amount, age):
        super().__init__(fname, lname, amount)
        self.age = age

    def withdraw(self, amount):
        if amount > 20000:
            raise ValueError ("Can not withdraw more than 20000 at once")
        super().withdraw(amount)


# cust1 = SavingsBankAccount("Mary", "Joseph", 30000)
# cust2 = SeniorCitizenAccount("John", "Patrick", 30000, 65)
#
# # # cust1.withdraw(12000)       # ValueError: Can not withdraw more than Rs.10000 at once
# # cust2.withdraw(12000)
# # cust2.statement()
#
# cust1.roi()
# cust2.roi()
#
# cust1.statement()
# cust2.statement()


class SukanyaSamruddhiAccount(BankAccount):
    interest_rate = 10
    def deposit(self, amount):
        if amount < 1000:
            raise ValueError ("Minimum deposit of Rs.1000 has to be done")
        super().deposit(amount)

    def withdraw(self, amount, age):
        if age < 18:
            raise Exception ("Can not withdraw before 18 years of age")
        super().withdraw(amount)

cust1 = SukanyaSamruddhiAccount("Mary", "Maria", 30000)
cust1.roi()
cust1.statement()