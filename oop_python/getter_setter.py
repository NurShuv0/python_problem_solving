class user:
    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self.__money = money

    @property
    def get_age(self):
        return self._age
    #setter conversion
    @get_age.setter
    def set_age(self, set_value):
        if set_value < 0:
            print("age can not be negative")
        else :
            self._age = set_value
    
    def get_salary(self, add):
        return self.__money + add

nur = user("nur", 22, 10000)
# print(nur.__money)
# print(nur._age)

# print(nur.get_age())

print(nur.get_age)
nur.set_age = 30
print(nur.set_age)
print(nur.get_salary(5000))
