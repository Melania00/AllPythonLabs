from abc import ABC, abstractmethod


class Fridge(ABC):
    def __init__(self, brand, model, capacity, is_defrosting, energy_efficiency_class, my_special_set):
        """
        Initialize the attributes of the fridge object
        """
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.is_defrosting = is_defrosting
        self.energy_efficiency_class = energy_efficiency_class
        self.my_special_set = my_special_set

    def __iter__(self):
        """Return an iterator over the features set."""
        return iter(self.my_special_set)

    @abstractmethod
    def turn_on_defrosting(self):
        """
        Abstract method that should be implemented by child classes
        """

    @abstractmethod
    def turn_off_defrosting(self):
        """
        Abstract method that should be implemented by child classes
        """

    @abstractmethod
    def get_max_usable_capacity(self):
        """
        Abstract method that should be implemented by child classes
        """

    def delete_model_info(self):
        """
        Non-abstract method that sets the model attribute to None
        """
        self.model = None

    def __dict_filter__(self, _type):
        """Filter dict keys and values by their types."""
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, _type):
                result[key] = value
        return result
