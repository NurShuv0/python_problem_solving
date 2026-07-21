class vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def move(self):
        return f'the bus is moving'
    
    def __repr__(self):
        return f"this is vahicle class and the name is {self.name} and the price is {self.price}"
    
class bus(vehicle):
    def __init__(self, name, price, seat):
        self.seat = seat
        super().__init__(name, price)

    def __repr__(self):
        return super().__repr__()
        # return "bus class"

class truck(vehicle):
    def __init__(self, name, price, weight):
        self.weight = weight
        super().__init__(name, price) 

class pickUp_truck(truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)


class AC_bus(bus):
    def __init__(self, name, price, seat, temperature):
        self.temperature = temperature
        super().__init__(name, price, seat)
    def __repr__(self):
        return super().__repr__()

vahicle_ob = vehicle("nur_vehicle", 1500)
print(vahicle_ob)

nur_bus = AC_bus("nur_bus", 1000, 20, 10)

print(nur_bus.move())
print(nur_bus.name)
print(nur_bus)
