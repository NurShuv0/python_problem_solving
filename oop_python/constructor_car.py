class car : 
    def __init__(self, brand, model, price):
        self.brand = brand
        self.price = price
        self.model = model

obj = car("marcedes", "nur_model", 2000000)
print(obj.brand, obj.model, obj.price)

obj2 = car("BMW", "Nur_bmw", 3000000)
print(obj2.brand, obj.model, obj2.price)
