from typing import Union

class Car:
    def __init__(self, brand: str, model: Union[str, int]):
        if not isinstance(model, (str, int)):
            raise TypeError("Model must be a string or integer")
        
        self.brand = brand
        self.model = model

    def start(self):
        return f"{self.brand} {self.model} is starting..."
    
class BMW(Car):

    def start(self):
        return f"{super().start()}\nPerforming BMW-specific diagnostics...\n"


class Tesla(Car):

    def start(self):
        return f"{super().start()}\nActivating self-driving systems...\n"
    

bmw = BMW("BMW", "X5")
tesla = Tesla("Tesla", 3)

print(bmw.start())
print(tesla.start())