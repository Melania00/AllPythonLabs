class Fridge:
    instance = None

    def __init__(self, brand, model, capacity, is_defrosting, energy_efficiency_class):
        self.__brand = brand
        self.__model = model
        self.__capacity = capacity
        self.__is_defrosting = is_defrosting
        self.__energy_efficiency_class = energy_efficiency_class

    @staticmethod
    def get_instance():
        if Fridge.instance is None:
            Fridge.instance = Fridge("Samsung", "RF28R7351SR", 32, True, "A")
        return Fridge.instance

    def turn_on_defrosting(self):
        self.__is_defrosting = True

    def turn_off_defrosting(self):
        self.__is_defrosting = False

    def delete_model_info(self):
        self.__model = None

    def __str__(self):
        return f"Fridge(Brand: {self.__brand}, Model: {self.__model}, Capacity (litres): {self.__capacity}," \
               f" Defrosting: {self.__is_defrosting}, Energy Efficiency Class: {self.__energy_efficiency_class})"
