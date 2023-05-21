from FridgeClass.models.FridgeCamera import FridgeCamera
from FridgeClass.models.WineFridge import WineFridge


class FridgeManager:
    def __init__(self):
        self.fridges = []

    def add_fridge(self, fridge):
        self.fridges.append(fridge)

    def find_samsung_fridges(self):
        return [f for f in self.fridges if f.brand == "Samsung"]

    def find_mechanical_drive_fridges(self):
        return [f for f in self.fridges if isinstance(f, FridgeCamera) and f.belt_drive_type == "mechanical"]

    def main(self):
        fridge_camera1 = FridgeCamera("Samsung", "FC1", 100, False, "A++", 2, "electrical", 3, 50)
        fridge_camera2 = FridgeCamera("LG", "FC2", 200, True, "A+", 3, "mechanical", 4, 100)
        wine_fridge1 = WineFridge("Bosch", "WF1", 50, False, "A++", 25, 0.75)
        wine_fridge2 = WineFridge("Samsung", "WF2", 80, True, "A++", 40, 0.75)

        self.add_fridge(fridge_camera1)
        self.add_fridge(fridge_camera2)
        self.add_fridge(wine_fridge1)
        self.add_fridge(wine_fridge2)

        """
        print all fridges
        """
        for fridge in self.fridges:
            print(fridge.__repr__)

        """
        search for Samsung fridges
        """
        samsung_fridges = self.find_samsung_fridges()
        print("\n\nSamsung Fridges:")
        for fridge in samsung_fridges:
            print(fridge.__repr__)

        """
        search for fridges with mechanical belt drive
        """
        find_mechanical_drive_fridges = self.find_mechanical_drive_fridges()
        print("\n\nMechanical Drive Fridges:")
        for fridge in find_mechanical_drive_fridges:
            print(fridge.__repr__)


if __name__ == "__main__":
    manager = FridgeManager()
    manager.main()
