from FridgeClass.models.fridge_camera import FridgeCamera
from FridgeClass.models.wine_fridge import WineFridge
from FridgeClass.managers.fridge_manager import FridgeManager
from FridgeClass.managers.set_manager import SetManager

"""
searching for samsung fridges
"""


def find_samsung_fridges(self):
    return [f for f in self.fridges if f.brand == "Samsung"]


"""
searching for mechanic drive type
"""


def find_mechanical_drive_fridges(self):
    return [f for f in self.fridges if isinstance(f, FridgeCamera) and f.belt_drive_type == "mechanical"]


def main():
    """
    Creating fridges objects
    """
    fridge_camera1 = FridgeCamera("Samsung", "FC1", 100, False, "A++", 2, "electrical", 3, 50)
    fridge_camera2 = FridgeCamera("LG", "FC2", 200, True, "A+", 3, "mechanical", 4, 100)
    wine_fridge1 = WineFridge("Bosch", "WF1", 0, False, "A++", 25, 0.75)
    wine_fridge2 = WineFridge("Samsung", "WF2", -5, True, "A++", 40, 0.75)
    fridges_manager = FridgeManager()
    fridges_manager.add_fridge(fridge_camera1)
    fridges_manager.add_fridge(fridge_camera2)
    fridges_manager.add_fridge(wine_fridge1)
    fridges_manager.add_fridge(wine_fridge2)

    fridges = fridges_manager.fridges
    result = list(fridges.get_max_usable_capacity() for fridge in fridges)
    print(result)

    result = [f"{fridge.title}: {index}" for index, fridge in enumerate(fridges)]
    print(result)

    fridge_connect_results = [fridge.get_max_usable_capacity() for fridge in fridges]
    result = [f"{fridge.title}: {connect_result}" for fridge, connect_result in zip(fridges, fridge_connect_results)]
    print(result)
