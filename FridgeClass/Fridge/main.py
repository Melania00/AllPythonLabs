from Fridge import Fridge


def main():
    fridges = [Fridge("LG", "LRMVC2306D", 23, False, "B"), Fridge("Apple", "RF28RGYHYYF", 40, True, "A++"),
               Fridge.get_instance(), Fridge.get_instance()]
    for fridge in fridges:
        print(fridge)


if __name__ == "__main__":
    main()
