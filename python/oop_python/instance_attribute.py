class shop :
    mall_name = "nur shopppin mall"
    # cart = []
    # price = []
    def __init__(self, name):
        self.name = name
        self.cart = []
        self.price = []
    
    def add_to_cart(self, item, price):
        self.cart.append(item)
        self.price.append(price)

nur_obj = shop("Nur")
nur_obj.add_to_cart("phone", 100000)
nur_obj.add_to_cart("watch", 5000)
nur_obj.add_to_cart("guiter", 10000)
print(nur_obj.name, "is buying ", nur_obj.cart, "\nprice are : ", nur_obj.price)

nirjon_obj = shop("nirjon")
nirjon_obj.add_to_cart("lipstick", 500)
nirjon_obj.add_to_cart("jama", 10000)
nirjon_obj.add_to_cart("shoes", 20000)
print(f"{nirjon_obj.name} is buying {nirjon_obj.cart}\nPrice are : {nirjon_obj.price}")