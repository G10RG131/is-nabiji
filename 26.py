import unittest
from vehicle import Vehicle, ElectricVehicle

class TestVehicle(unittest.TestCase):

    def test_vehicle_fuel_up(self):
        vehicle = Vehicle("Ford", "Focus", 2022)
        self.assertEqual(vehicle.fuel_up, "Gas tank is now full or can move.")

    def test_vehicle_drive(self):
        vehicle = Vehicle("Ford", "Focus", 2022)
        self.assertEqual(vehicle.drive, "The Focus is now driving.")

    def test_electric_vehicle_charge(self):
        ev = ElectricVehicle("Tesla", "Model 3", 2023)
        self.assertEqual(ev.charge, "The vehicle is now charged.")

    def test_electric_vehicle_fuel_up(self):
        ev = ElectricVehicle("Tesla", "Model 3", 2023)
        self.assertEqual(ev.fuel_up, "This vehicle has no fuel tank!")

if __name__ == '__main__':
   
    print(help(Vehicle))
    print(help(ElectricVehicle))
    unittest.main()
