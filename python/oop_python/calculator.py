class calculator : 
    brand = "nur calculator"

    def sum(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        return a / b


obj = calculator()
print("The calculator brand is ", obj.brand)
print("press 1 for sum, 2 for sub, 3 for mul, 4 for division")
n = int(input())
num1, num2 = map(int, input("enter the numbers : ").split())
if n == 1: 
    result = obj.sum(num1, num2)
    print(result)
elif n == 2:
    result = obj.sub(num1, num2)
    print(result)
elif n == 3:
    result = obj.mul(num1, num2)
    print(result)
elif n == 4:
    result = obj.div(num1, num2)
    print(result)

