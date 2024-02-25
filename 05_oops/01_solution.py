class CarInfo :
    def __init__(self, userBrand , userModel):
        self.__brand = userBrand
        self.model = userModel

    def get_brand(self):
        return f"{self.__brand} !"  

    def fuelType(self):
        return "petrol or diesel !"  

    def fullName(self):
        return f"{self.__brand} {self.model}"    


# my_car = CarInfo("toyota", "Supra")
# print("Brand :" ,my_car.brand)
# print("model :" ,my_car.model)
# print(my_car.fullName())

# my_new_car = CarInfo("Tata", "Safari")
# print("Brand :" ,my_new_car.brand)
# print("model :" ,my_new_car.model)


class ElectricCar(CarInfo):
    def __init__(self , userBrand ,userModel ,batterySize):
        super().__init__(userBrand ,userModel)
        self.batterySize = batterySize

    def fuelType(self):
        return "Electric Charge!" 

tesla = ElectricCar("tesla" ,"cybertruck","55kWh") 
print(tesla.get_brand())
# print(tesla.model)
# print(tesla.batterySize)
# print(tesla.fullName())
print(tesla.fuelType())

