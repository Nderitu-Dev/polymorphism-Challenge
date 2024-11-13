class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("The car is driving 🚗!")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying ✈️!")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing 🚤!")

# Example usage:
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  # Polymorphism in action
