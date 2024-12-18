
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def chai_brand(self):
        return self.brand + " !"

    def fullname(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.chai_brand()) # can access function of parent class
# print(my_tesla.fuel_type()) # it will get its own function(first it will search within it's own class)


# my_car = Car("Tata", "Safari")
# my_car.model = "City"
# Car("Tata", "Nexon")

my_car = Car("Toyoto", "Corolla")
Car("Tata", "Nexon")

# print(my_car.general_description())
# print(Car.general_description())



# Acessing Model
# print(my_car.model)


# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)



class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
# print(my_new_tesla.engine_info())
# print(my_new_tesla.battery_info())