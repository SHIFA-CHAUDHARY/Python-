class Car:
    total_car = 0
    

    def __init__(self,brand,model):
        self.__brand= brand #private (class kai andr hi access milega)
        self.__model = model
        Car.total_car = self.total_car + 1
    @staticmethod  
    def general_description():
        return "Cars are means of Transport"
    
    @property
    def model(self):
        return self.__model
    
    def get_brand(self):
        return self.__brand + "!"
        
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self ,brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric charge"
    
class battery:
    def battery_info(self):
        return "this in battery"
    

class Engine:
    def engine_battery(self):
        return "this is engine"

class ElectricCarTwo(battery,Engine,Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model s")

print(my_new_tesla.battery_info())
print(my_new_tesla.engine_battery())