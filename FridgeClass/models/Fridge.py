from abc import ABC, abstractmethod


class Fridge(ABC):
    def __init__(self, brand, model, capacity, is_defrosting, energy_efficiency_class):
        """
        Initialize the attributes of the fridge object
        """
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.is_defrosting = is_defrosting
        self.energy_efficiency_class = energy_efficiency_class

    @abstractmethod
    def turn_on_defrosting(self):
        """
        Abstract method that should be implemented by child classes
        """
        pass

    @abstractmethod
    def turn_off_defrosting(self):
        """
        Abstract method that should be implemented by child classes
        """
        pass

    @abstractmethod
    def get_max_usable_capacity(self):
        """
        Abstract method that should be implemented by child classes
        """
    pass

    def delete_model_info(self):
        """
        Non-abstract method that sets the model attribute to None
        """
        self.model = None
