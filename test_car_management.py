import unittest
from car_management import Car, CarManagement

class TestCarManagement(unittest.TestCase):
    
    def setUp(self):
        """Set up a fresh instance for each test."""
        self.manager = CarManagement()
        self.car1 = Car(1, "Toyota", "Corolla", 2020)
        self.car2 = Car(2, "Honda", "Civic", 2022)

    def test_add_car(self):
        """Test adding a car to the system."""
        result = self.manager.add_car(self.car1)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.cars), 1)

    def test_add_duplicate_car(self):
        """Test adding a car with duplicate ID."""
        self.manager.add_car(self.car1)
        with self.assertRaises(ValueError):
            self.manager.add_car(self.car1)

    def test_remove_car(self):
        """Test removing a car."""
        self.manager.add_car(self.car1)
        result = self.manager.remove_car(self.car1.car_id)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.cars), 0)

    def test_remove_nonexistent_car(self):
        """Test removing a car that doesn't exist."""
        with self.assertRaises(ValueError):
            self.manager.remove_car(100)

    def test_get_car(self):
        """Test retrieving car details."""
        self.manager.add_car(self.car1)
        car = self.manager.get_car(1)
        self.assertIsNotNone(car)
        self.assertEqual(car.brand, "Toyota")

    def test_get_nonexistent_car(self):
        """Test getting a car that doesn’t exist."""
        car = self.manager.get_car(100)
        self.assertIsNone(car)

if __name__ == "__main__":
    unittest.main()
