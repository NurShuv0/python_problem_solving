class bank:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
    
    # def __repr__(self):
    #     return "hello"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            return amount
        else :
            return "not enough money"
    
    def get_balance(self):
        return self.__balance
    
nur = bank("nur", 10000)
# print(nur.__name)
# print(nur._bank__balance)
print(nur.get_balance())
print(nur.withdraw(500))