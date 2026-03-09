class bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 500
        self.max_withdraw = 100000

    def get_balance(self):
        if self.balance > 0:
            return self.balance
        else: 
            return "you gorib"
    
    def deposit(self, amount):
        if amount > 0: 
            self.balance += amount
            print("Now your balance is : ", self.get_balance())
        else:
            print("check the amount again")
    
    def withdraw(self, amount):
        if amount > self.max_withdraw:
            print("sorry max withdraw is ",self.max_withdraw)
        elif amount < self.min_withdraw:
            print("sorry min withdraw ammount is ", self.min_withdraw)
        else :
            self.balance -= amount
            print("now your balance is : ", self.get_balance())

nur_bank = bank(10000)
nur_bank.deposit(2000)
nur_bank.deposit(5000)
nur_bank.withdraw(3000)
nur_bank.withdraw(-111)
nur_bank.withdraw(1000000)
nur_bank.withdraw(3000)


goriber_bank = bank(100500)
goriber_bank.deposit(200)
goriber_bank.deposit(5000)
goriber_bank.withdraw(4000)
goriber_bank.withdraw(0)
goriber_bank.withdraw(1000000)
goriber_bank.withdraw(6000)
goriber_bank.withdraw(100000)

    