class Fridge:
    instance = None

    def __init__(self, brand, model, capacity, is_defrosting, energy_efficiency_class):
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.is_defrosting = is_defrosting
        self.energy_efficiency_class = energy_efficiency_class

    @staticmethod
    def get_instance():
        if Fridge.instance is None:
            Fridge.instance = Fridge("Samsung", "RF28R7351SR", 32, True, "A")
        return Fridge.instance

    def turn_on_defrosting(self):
        self.is_defrosting = True

    def turn_off_defrosting(self):
        self.is_defrosting = False

    def delete_model_info(self):
        self.model = None


def main():
    fridge1 = Fridge("Samsung", "RF28R7351SR", 32, True, "A")
    fridge2 = Fridge("LG", "LRMVC2306D", 23, False, "B")
    fridge3 = Fridge.get_instance()
    fridge4 = Fridge.get_instance()

    print("Brand:", fridge1.brand)
    print("Model:", fridge1.model)
    print("Capacity (liters):", fridge1.capacity)
    print("Defrosting Enabled:", fridge1.is_defrosting)
    print("Energy Efficiency Class:", fridge1.energy_efficiency_class)
    print(" ")

    print("Brand:", fridge2.brand)
    print("Model:", fridge2.model)
    print("Capacity (liters):", fridge2.capacity)
    print("Defrosting Enabled:", fridge2.is_defrosting)
    print("Energy Efficiency Class:", fridge2.energy_efficiency_class)
    print(" ")

    print("Brand:", fridge3.brand)
    print("Model:", fridge3.model)
    print("Capacity (liters):", fridge3.capacity)
    print("Defrosting Enabled:", fridge3.is_defrosting)
    print("Energy Efficiency Class:", fridge3.energy_efficiency_class)
    print(" ")

    print("Brand:", fridge4.brand)
    print("Model:", fridge4.model)
    print("Capacity (liters):", fridge4.capacity)
    print("Defrosting Enabled:", fridge4.is_defrosting)
    print("Energy Efficiency Class:", fridge4.energy_efficiency_class)
    print(" ")


if __name__ == "__main__":
    main()
