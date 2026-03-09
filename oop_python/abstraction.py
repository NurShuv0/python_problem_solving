from abc import abstractmethod,ABC

class animal(ABC):
    @abstractmethod
    def eat(self):
        print("animal eats")
    
    def move(self):
        print("animals moves")
    
class monkey(animal):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("monkey eats")

class tiger(animal):
    def __init__(self, name,age):
        self.name = name
        self.age = age
        super().__init__()
    def eat(self):
        print("tiger eats")
    def test(self):
        print("test successfull")

mnk = monkey("rocky_monkey")
mnk.move()
tgr = tiger("rokey tiger", 10)
tgr.move()
tgr.test()

# anim = animal()
# anim.test()
