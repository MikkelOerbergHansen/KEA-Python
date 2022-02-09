# class example

#definer en class
class Car:
    def __init__(self, color, brand, model):
        self.color = color                  # definer Attributter
        self.brand = brand
        self.model = model


#definer en variabel af vores Car class
car1 = Car("Green", "volkswagen", "Golf")
car2 = Car("Blue", "Toyota", "Prius")
car3 = Car("Red", "Ford", "Mustang")

#print værdier for valgte attributter på de valgte variable
print(car1.brand)
print(car2.brand)
print(car3.brand)