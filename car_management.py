class Car:
    def __init__(self, car_id, brand, model, year):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year

    def __repr__(self):
        return f"{self.year} {self.brand} {self.model} (ID: {self.car_id})"

class CarManagement:
    def __init__(self):
        self.cars = {}

    def add_car(self, car):
        """Adds a car to the system."""
        if car.car_id in self.cars:
            raise ValueError("Car ID already exists.")
        self.cars[car.car_id] = car
        return True

    def remove_car(self, car_id):
        """Removes a car from the system."""
        if car_id not in self.cars:
            raise ValueError("Car not found.")
        del self.cars[car_id]
        return True

    def get_car(self, car_id):
        """Retrieves a car's details."""
        return self.cars.get(car_id, None)
