class shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
    def add_to_cart(self, item, price, quantity):
        product = {
            "item":item,
            "price":price,
            "quantity":quantity
        }  
        self.cart.append(product)
        # print(self.cart)
    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item["price"] * item['quantity']
        print("total amount is : ", total )
        if total < amount:
            print(f"take the change of {amount - total} taka")
        else :
            print(f'give me more {total - amount} taka')



nur = shopping("Nur the gorib")
nur.add_to_cart("guiter", 10000, 2)
nur.add_to_cart("suit", 5000, 2)
nur.add_to_cart("perfume", 500, 5)

print(nur.cart)

nur.checkout(20000)
nur.checkout(50000)