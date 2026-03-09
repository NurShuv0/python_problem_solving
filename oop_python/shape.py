from math import pi
class shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        print("it will call if the chile class has no area function")

class rectrangle(shape):
    def __init__(self, name, height, width):
        self.height = height
        self.width = width
        super().__init__(name)
    def area(self):
        return self.height * self.width
    
class circle(shape):
    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)
    
    def area(self):
        return 2 * pi * self.radius**2

class triangle(shape):
    def __init__(self, name, vhumi, height):
        self.vhumi = vhumi
        self.height = height
        super().__init__(name)

    def area(self):
        return .5 * self.vhumi *self.height 

obj_circle = circle("circle",5)
obj_triangle = triangle("triangle",10, 20)
obj_rec = rectrangle("rectrangle",100, 200)


obj_list = [obj_circle, obj_rec,obj_triangle]
for i in obj_list:
    print(i.area())

# print(obj_circle.area())
# print(obj_triangle.area())
# print(obj_rec.area())




        