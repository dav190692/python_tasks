import math

#task1-4

class Vehicel:
    vehicle_count = 0

    
    def __init__(self, make:int , model:str):
        self.__make = make
        self.__model = model
        self.increment_vehicle_count()
        

    def __repr__(self) -> str:
        return f"Vehicel(make = {self.__make}, model = {self.__model})"

    def increment_vehicle_count(self) -> None:
        Vehicel.vehicle_count += 1

    def get_vehicle_count(self)->int:
        return Vehicel.vehicle_count


    def set_make (self, value:int) -> None:
        if value == "" and  not isinstance(value, int):
            raise ValueError('Please type corect value')
        self.__make = value
    
    def set_model (self, value:str)->None:
        if value == "" and not isinstance(value, str):
            raise ValueError('Please type corect value')
        self.__model = value
    
    def get_make (self):
        return self.__make

    def get_model (self):
        return self.__model 
    
    def start_engine(self):
        print("Engine started")
    
class Car(Vehicel):
    def __init__(self, make, model, number_of_wheels):
        super().__init__(make, model)
        self.__number_of_wheels = number_of_wheels
        super().start_engine()

    def __repr__(self) -> str:
        return f"Car(make = {self.get_make()}, model = {self.get_model()}, number_of_wheels = {self.__number_of_wheels})"

    def set_number_of_wheels (self, value):
        if value < 0 or value == "" or not isinstance(value, int):
            raise ValueError('Please type corect value')
        self.__number_of_wheels = value

    def get_number_of_wheels(self):
        return self.__number_of_wheels


class ElectricVehicle:
    def __init__(self, battery_capacity) -> None:
        self.__battery_capacity = battery_capacity

    def set_battery_capacity(self, value):
        self.__battery_capacity = value
    
    def get_battery_capacity(self):
        return self.__battery_capacity
    

class ElectricCar(Car, ElectricVehicle):
    def __init (self, make, model, number_of_wheels,battery_capacity ):
        super().__init__(make, model,number_of_wheels)
        ElectricVehicle.__init__(self, battery_capacity)
#_____________________________________________________
print(ElectricCar.__mro__)
# electric_car1 = ElectricCar(1999, 'model_x', 4, "12v")
electric_car1 = ElectricCar(1999, 'model_x', 4,)
electric_car1.set_battery_capacity("12v")
print(electric_car1.get_battery_capacity())
print("\n")
#_________________________________
vehicle1 = Vehicel(1998, 'model1')
print(vehicle1.get_model())
vehicle1.set_model("model2")
print(vehicle1.get_model())
print(vehicle1.get_vehicle_count())
print(vehicle1)
print("\n")
#_____________________________________
car1 = Car(2014, 'model3', 4)
print(car1.get_model())
print(car1.get_make())
print(car1.get_vehicle_count())
print(car1)
print("\n")
#________________________________________
car2 = Car(1992, "model4", 2025)
print(car2.get_vehicle_count())
car2.set_number_of_wheels(2)
print(car2)
print("\n")
#___________________________________________

#task 1-4 end

#task5

class Polar:
    def __init__(self, radius, angle):
        self.__radius = radius
        self.__angle = angle
    
    def __repr__(self) -> str:
        return f"Polar object radius = {self.__radius}, angle = {self.__angle}"
    

    def set_radius(self, value):
        if value == "" or not isinstance(value, int):
            raise ValueError("Type corect value please")
        self.__radius = value

    def get_radius(self):
        return self.__radius
    
    def set_angle(self, value):
        if value == "" or not isinstance(value, int):
            raise ValueError("Type corect value please")
        self.__angle = value

    def get_angle(self, value):
        return self.__angle   
    
   
    def to_rectangular(self):
        x = self.__radius * math.cos(math.radians(self.__angle))
        y = self.__radius * math.sin(math.radians(self.__angle))
        return x, y

    
    def from_rectangular(x, y):
        radius = math.sqrt(x ** 2 + y ** 2)
        angle = math.degrees(math.atan2(y, x))
        return Polar(radius, angle)

    def __add__(self, other):
        x1, y1 = self.to_rectangular()
        x2, y2 = other.to_rectangular()
        x_sum = x1 + x2
        y_sum = y1 + y2
        return Polar.from_rectangular(x_sum, y_sum)
    

polar1 = Polar(3, 90)
polar2 = Polar(2, 30)

print(repr(polar1))
print(repr(polar2))

polar3 = polar1 + polar2

print(polar3)