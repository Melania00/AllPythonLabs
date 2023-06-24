class FridgeManager:
    def __init__(self):
        self.fridges = []

    def add_fridge(self, fridge):
        self.fridges.append(fridge)

    def __len__(self):
        return len(self.fridges)

    def __getitem__(self, index):
        return self.fridges[index]

    def __iter__(self):
        return iter(self.fridges)

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

    def main(self):
        pass
