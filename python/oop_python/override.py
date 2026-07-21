class person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("person eats")
    def sleep(self):
        print("person sleeps")

    def exercise(self):
        raise NotImplementedError

class cricketer(person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)

    # def eat(self):
    #     print("player eats")

    def exercise(self):
        print("player exercise")

per_obj = person("nur",22, 69, 65)
per_obj.eat()

sakib = cricketer("sakib", 22, 55, 77, "BD")

sakib.eat()
sakib.exercise()
