import datetime


class Car (object):
    number_of_cars = 0

    def __init__(self, brand, model, manufacturing_year):
        self.Brand = brand
        self.Model = model
        self.Year = manufacturing_year
        Car.number_of_cars += 1

    def car_info(self):
        print(self.Brand, self.Model, self.Year)

    def age_of_car(self):
        print(datetime.date.today().year - self.Year)

    @staticmethod
    def total_cars():
        print(Car.number_of_cars)


class Electric_Car(Car):
    def __init__(self, brand, model, manufacturing_year, battery_life):
        super().__init__(brand, model, manufacturing_year)
        self.Battery_life = battery_life

    def battery_info(self):
        print("ამ მანქანის ბატარეის ხანგრძლივობა არის", self.Battery_life, "საათი")


c1 = Car('Ford', 'Mustang', 1969)
c3 = Car('Ford', 'Focus', 1999)
c4 = Car('Ford', 'Fusion', 2015)
c5 = Car('Ford', 'Mach-e', 2020)
c2 = Electric_Car('Tesla', 'model x', 2021, 100)

c1.car_info()
c2.car_info()
c1.age_of_car()
c2.age_of_car()
c3.age_of_car()
c4.age_of_car()
c5.age_of_car()
print(Car.total_cars())
