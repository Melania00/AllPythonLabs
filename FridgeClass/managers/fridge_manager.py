class FridgeManager:
    """
    creating constructor for the class and list of obj
    """
    def __init__(self):
        self.fridges = []
    """"
    function for adding fridges to the list
    """
    def add_fridge(self, fridge):
        self.fridges.append(fridge)
    """
    discovering the length of obj
    """
    def __len__(self):
        return len(self.fridges)

    def __getitem__(self, index):
        return self.fridges[index]

    def __iter__(self):
        return self
    """
    executing method
    """
    def execute_method(self, method_name):
        result = [getattr(f, method_name)() for f in self.fridges if hasattr(f, method_name)]
        return result

    def concatenate_with_index(self):
        result = ["[{}]{}".format(i, f) for i, f in enumerate(self.fridges)]
        return result

    def paste_with_method(self, method_name):
        result = ["{}({})".format(f, getattr(f, method_name)()) for f in self.fridges if hasattr(f, method_name)]
        return result

    def dict_with_type(self, data_type: type):
        result = {}
        for f in self.fridges:
            result.update({k: v for k, v in f.__dict__.items() if isinstance(v, data_type)})
        return result

    def all_any(self, method_name):
        """"
        The getattr() method returns the value of the named attribute of an object.
        The hasattr() method returns true if an object has the given named attribute and false if it does not.
        """
        all_result = all(getattr(f, method_name)() for f in self.fridges if hasattr(f, method_name))
        any_result = any(getattr(f, method_name)() for f in self.fridges if hasattr(f, method_name))
        return {"all": all_result, "any": any_result}

    def execute_abstract_method(self, method_name):
        return [f.execute_method(method_name) for f in self.fridges if hasattr(f, method_name)]

    def concatenate_with_serial_number(self):
        return ["[{}] {}".format(i, f) for i, f in enumerate(self.fridges)]

    def paste_with_abstract_method(self, method_name):
        return ["{}({})".format(f, f.execute_method(method_name)) for f in self.fridges if hasattr(f, method_name)]

    def dict_with_type_abstract(self, data_type: type):
        result = {}
        for f in self.fridges:
            result.update({k: v for k, v in f.__dict__.items() if isinstance(v, data_type)})
        for f in self.fridges:
            result.update(
                {k: v for k, v in f.execute_method("get_attributes_dict").items() if isinstance(v, data_type)})
        return result

    def all_any_abstract(self, method_name):
        all_result = all(f.execute_method(method_name) for f in self.fridges if hasattr(f, method_name))
        any_result = any(f.execute_method(method_name) for f in self.fridges if hasattr(f, method_name))
        return {"all": all_result, "any": any_result}

    def print_dict_filter(self, _type):
        """Print filtered dictionary."""
        for fridge in self.fridges:
            print(f"\n{type(fridge).__name__} {fridge.brand}")
            print(fridge.__dict_filter__(_type))

    def main(self):
        pass
