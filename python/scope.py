balance = 10000
def buy_things(item, price):
    global balance
    balance -= price
    # print(item, "the balance is : ",balance)
    print(f"the balance inside the method is : {balance}")

print("balance in outside of the method is ", balance)
buy_things('bike', 5000)