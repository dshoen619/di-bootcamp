class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def str(self):
        print(f"{self.amount} {self.currency}'s ") 

    def int(self):
        print(self.amount.__int__())

    def repr(self):
        print(repr(f"{self.amount} {self.currency}'s"))

    
    def add(self,amount):
        print(self.amount+amount)

    def add_wallets(self,other):
        if self.currency==other.currency:
            print(self.amount+other.amount)
        else:
            raise TypeError("Different Currencies cannot be added")

    def wallet_in_initial_form(self):
        print(self.amount,f"{self.currency}'s")

    def add_to(self,amount):
        self.amount+=amount


c1=Currency('dollar', 5)
c2 = Currency('dollar', 10)

c1.str()
c1.int()
c1.repr()

c1.add_wallets(c2)
c1.wallet_in_initial_form()
c1.add_to(15)
print(c1.amount)