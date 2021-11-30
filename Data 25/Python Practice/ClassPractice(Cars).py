class Car:
    def __init__(self, year, make, colour, max_speed):
        self.year_model = year
        self.make = make
        self.colour = colour
        self.max_speed = max_speed
        self.speed = 0
        # self.miles = 0

    def set_year_model(self, year):
        self.year_model = year

    def set_make(self, make):
        self.make = make

    def set_speed(self, speed):
        self.speed = 0

    def get_year_model(self):
        return self.year_model

    def get_make(self):
        return self.make

    def get_speed(self):
        return self.speed

    def accelerate(self, acceleration):
        if self.speed + acceleration > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += acceleration

    def brake(self, brake):
        if self.speed - brake < 0:
            self.speed = 0
        else:
            self.speed -= brake

    # def mileage(self, miles):
    #     return self.miles


jade_Car = Car(2019, 'audi', "Teal", 150)
jen_Car = Car(2020, 'bmw', "Blue", 170)
# jen_Car.mileage(10)
# print(f"Jen's car has gone {jen_Car.mileage}miles.")
print(f"Jade's car is currently going {jade_Car.speed}mph.")
jade_Car.accelerate((160))
jen_Car.accelerate(20)
print(f"Jade's car is currently going {jade_Car.speed}mph.")
print(f"Jen's car is currently going {jen_Car.speed}mph.")
jade_Car.accelerate(70)
print(f"Jade's car is currently going {jade_Car.speed}mph.")
jade_Car.set_year_model(1999)
print(f"The year model of Jade's car is {jade_Car.year_model}.")