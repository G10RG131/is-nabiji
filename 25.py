from abc import ABC, abstractmethod

# TODO SOLID პრინციპის დაცვით შეცვალეთ კლასების იმპლემენტაცია

# Single Responsibility Principle
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


    def get_discount_price(self, discount):
        if discount < 0 or discount > 100:
            return "Invalid discount. Please provide a value between 0 and 100."
        return (self.price * (100 - discount))/100




# TODO დაამატეთ  PayPal-ის გადახდების კლასი, და  Payment
# Open/Closed Principle
class Payment(ABC):
    """  გადახდის კლასი საკრედიტო ბარათით გადახდების დასამუშავებლად
    """
    @abstractmethod
    def process_credit(self, amount):
        ...

class PayPal(Payment):
    def __int__(self, balance):
        self.balance = balance

    def process_credit(self, amount):
        self.balance -= amount


# TODO გადააკეთეთ კლასები ისე, რომ დაიცვან ლისკოვის ჩანაცვლების პრინციპი
# Liskov Substitution Principle
class Vehicle:
    @abstractmethod
    def fuel_capacity(self):
        return "100 liters"

class ElectricCar(Vehicle):
    def fuel_capacity(self):
        return "Battery capacity is 100 kWh"


# TODO შეცვალეთ იმპლემენტაცია, რადგან ყველა მოთამაშეს არ აქვს აუდიოს ან ვიდეოს მხარდაჭერა
# Interface Segregation Principle
class play_audio(ABC):
    @abstractmethod
    def play_audio(self):
        ...
class play_video(ABC):
    @abstractmethod
    def play_video(self):
        ...

class SvenMC(play_audio):
  def play_audio(self):
    print("Stereo")


class SamsungOdyssey(play_video):
  def play_video(self):
    print("Monitor")



# TODO შეცვალეთ კლასის იმპლემენტაცია, რომ დაიცვას დამოკიდებულების ინვერსიის პრინციპი.
# Dependency Inversion Principle (DIP)

class Switchable(ABC):
  @abstractmethod
  def operate(self, on_off: bool):
    ...

class Switch:
    @staticmethod
    def controller(device: Switchable, on_off=True):
        device.operate(on_off)

class ConsoleDisplay(Switchable):
    def operate(self, on_off: bool, data=None):
        if on_off:
            self.show(data)
        else:
            print("Display is Off")
    @staticmethod
    def show(data):
        print(data)

class WeatherStation(Switchable):
    def operate(self, on_off: bool):
        if on_off:
            self.report(ConsoleDisplay)
        else:
            print("Display is Off")
    @staticmethod
    def report(display):
        display.show("Weather Data")

