#has a relation purpose
class shopping:
    cart = []
    origin = "no origin"

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def purchase(self, item, price, amount):
        remaining = (amount - price)
        print(f"buying {item} for price : {price} and the remaining is {remaining}")

    @staticmethod
    def static_test(a, b):
        print(f'static output is : {a * b}')
        # print(self.location)

    @classmethod
    def class_method_test(self, a, b):
        print(f"class method output is : {a + b}")
 
bashundhara = shopping("bashundhara", "amar bashar chade")
print(bashundhara.name)
# shopping.purchase("phone", 10000, 20000)
bashundhara.purchase("phone", 5000, 10000)

shopping.class_method_test(10, 20)

shopping.static_test(100, 200)

        
