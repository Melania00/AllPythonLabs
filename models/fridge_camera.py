from typing import Final
from models.fridge import Fridge


class FridgeCamera(Fridge):
    VOLUME_PER_KILOGRAM: Final[int] = 0.25

    def __init__(self, brand, model, capacity, is_defrosting, energy_efficiency_class, num_inputs, belt_drive_type,
                 belt_speed, max_weight):
        super().__init__(brand, model, capacity, is_defrosting, energy_efficiency_class)
        self.num_inputs = num_inputs
        self.belt_drive_type = belt_drive_type
        self.belt_speed = belt_speed
        self.max_weight = max_weight

    def turn_on_defrosting(self):
        return self.is_defrosting(True)

    def turn_off_defrosting(self):
        return self.is_defrosting(False)

    def get_max_usable_capacity(self):
        return self.capacity * self.VOLUME_PER_KILOGRAM

    def __repr__(self):
        return f"\nFridgeCamera - Brand: {self.brand}, Model: {self.model}, Capacity in litres: {self.capacity} L\n" \
               f" Is defrosting: {self.is_defrosting}, Energy capacity class: {self.energy_efficiency_class}\n"\
               f" Num Inputs: {self.num_inputs}, Belt Drive Type: {self.belt_drive_type}\n" \
               f" Belt Speed: {self.belt_speed} m/s, Max Weight: {self.max_weight} kg"
