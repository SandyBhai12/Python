class Car:
    def __init__(self,type):
        self.type=type

    def start(self):
        print("start the car")

    def stop(self):
        print("stop the car")

class ToyotaCar(Car):
    def __init__(self, type,brand):
        super().__init__(type)
        self.brand=brand

# t=ToyotaCar("carType","fourunater")
# print(t.type)
# print(t.brand)

class Person:
    name="something"

    @classmethod
    def changeName(self,name):
        self.name=name

p=Person()
p.name="sandeep"
# Person.name="Sandeep"
p.changeName("sandeep")
print(Person.name)


