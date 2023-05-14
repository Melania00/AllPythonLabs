class Fridge:
    def __init__(self, brand, model, capacity, is_defrosting, energy_efficiency_class):
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.is_defrosting = is_defrosting
        self.energy_efficiency_class = energy_efficiency_class

    def turn_on_defrosting(self):
        self.is_defrosting = True

    def turn_off_defrosting(self):
        self.is_defrosting = False

    def delete_model_info(self):
        self.model = None


def main():
    my_fridge = Fridge("Samsung", "RF28R7351SR", 32, True, "A")

    print("Brand:", my_fridge.brand)
    print("Model:", my_fridge.model)
    print("Capacity (liters):", my_fridge.capacity)
    print("Defrosting Enabled:", my_fridge.is_defrosting)
    print("Energy Efficiency Class:", my_fridge.energy_efficiency_class)


if __name__ == "__main__":
    main()
