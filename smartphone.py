class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in percentage
        self.is_on = False
        self.features = ["Call", "Text", "Internet"]

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def charge(self):
        self.battery_life = 100
        print(f"{self.brand} {self.model} is fully charged!")

    def show_features(self):
        print(f"Features of {self.brand} {self.model}: {', '.join(self.features)}")

# Example usage:
phone = Smartphone("Apple", "iPhone 14", 50)
phone.turn_on()
phone.show_features()
phone.charge()
