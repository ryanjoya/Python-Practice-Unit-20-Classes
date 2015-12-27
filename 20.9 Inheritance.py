class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
    def drive_car(self):
        self.condition = "used"

my_car = Car("DeLorean", "silver", 88)
print my_car.condition

my_car.drive_car()

print my_car.condition

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type = battery_type
my_car = ElectricCar("Tesla", "black", 500, "molten salt")
print my_car.model
print my_car.color
print my_car.mpg
print my_car.battery_type
