from FridgeClass.models.fridge import Fridge


class WineFridge(Fridge):
    def __init__(self, brand: str, model, capacity, is_defrosting, energy_efficiency_class, max_num_bottles,
                 max_bottle_volume):
        my_special_set = {"my special fridge"}
        super().__init__(brand, model, capacity, is_defrosting, energy_efficiency_class, my_special_set)
        self.max_num_bottles = max_num_bottles
        self.max_bottle_volume = max_bottle_volume

    def turn_on_defrosting(self):
        return self.is_defrosting(True)

    def turn_off_defrosting(self):
        return self.is_defrosting(False)

    def get_max_usable_capacity(self):
        return self.capacity

    def __repr__(self):
        return f"\nWineFridge - Brand: {self.brand}, Model: {self.model}, Capacity in litres: {self.capacity} L\n" \
               f" Is defrosting: {self.is_defrosting}, Energy capacity class: {self.energy_efficiency_class}\n"\
               f" Max Num Bottles: {self.max_num_bottles}, Max Bottle Volume: {self.max_bottle_volume} L"
