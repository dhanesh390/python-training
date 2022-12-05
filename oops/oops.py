from abc import ABC, abstractmethod

"""
 This class represents the attributes of car object
"""


# class Car:
#     car_type = 'Electric car'  # Class attribute
#
#     def __init__(self, name, color, model, fuel_capacity, price):
#         self.price = price
#         self.__name = name
#         self._color = color  # Instance attribute
#         self.model = model
#         self.fuel_capacity = fuel_capacity
#
#     @classmethod
#     def status(cls, status):
#         """
#         This is a class method, which as access to the class objects
#         :param status:
#         :return:
#         """
#         cls.status = status
#
#     def discription(self):
#         return f'The {self.__name} car is a {self.car_type}, it model is {self.model}'
#
#     def date_of_availability(self, date_of_availability):
#         return f'The car {self.car_type} is available from {date_of_availability}'
#
#     @staticmethod
#     def calculate_tax(price, cgst, sgst):
#         sum = cgst * price + sgst * price
#         return f'The total tax for the car {sum}'
#
#
# class Properties(Car):
#
#     def __init__(self, name, color, model, fuel_capacity, seat_capacity, price):
#         super().__init__(name, color, model, fuel_capacity, price)
#         self.seat_capacity = seat_capacity
#
#     def capacity(self):
#         return f'The car {self.__name} is a {self.seat_capacity}'
#
#
# first_car = Car('Tesla', 'black', 'Ev-5', '200km', '40L')
# print(first_car.discription())
# print(first_car.date_of_availability('20.12.22'))
# print('2', first_car._Car__name)
# print(first_car.calculate_tax(3000000, 20000, 15000))
#
#
# # audi = Properties('Audi', 'black', 'a-5', '300km', '2-seater', '39L')
#
#
# # print('1', audi.capacity()


class Vehicle(ABC):
    """ This class represents the vechile object """
    # class variables belongs to the class
    vehicle_manufactured_at = 'India'

    def __init__(self, vehicle_type, vehicle_name, vehicle_model_name, vehicle_color, vehicle_price, quantity):
        """ The constructor contains the properties of the vechile class"""
        self.total_price = None
        self.__discount = None
        self.vehicle_type = vehicle_type
        self.vehicle_name = vehicle_name
        self.vehicle_model_name = vehicle_model_name  # Instance variables belongs to instance of the class
        self.vehicle_color = vehicle_color
        self.__vehicle_price = vehicle_price
        self.quantity = quantity

    def set_vehicle_name(self, vehicle_name):
        self.vehicle_name = vehicle_name

    def get_vehicle_name(self):
        return self.vehicle_name

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__vehicle_price * (1 - self.__discount)
        return self.__vehicle_price

    def __repr__(self):
        return f'The vechile {self.vehicle_name} of model {self.vehicle_model_name} cost around {self.__vehicle_price}'

    @abstractmethod
    def description(self):
        return f'This vechile {self.vehicle_name} of model {self.vehicle_model_name} is manufactured in' \
               f' {self.vehicle_manufactured_at}'

    def get_total_price(self):
        return self.total_price

    @staticmethod
    def calculate_tax(price, c_gst, s_gst):
        print(f'{Vehicle.vehicle_manufactured_at}')
        total_price = (c_gst * price) + (s_gst * price)
        return total_price

    @classmethod
    def year_of_manufacturing(cls, manufactured_year):
        print(f'{Vehicle.vehicle_manufactured_at}')
        cls.manufactured_year = manufactured_year

    def __del__(self):
        return 'Instance deleted'


"""
 This class inherits the Vehicle class which allows the child class Car to have access to its attributes
"""


class Car(Vehicle):
    """ This class represents the car object it is the child class to the parent class vechile"""

    def __init__(self, vehicle_type, vehicle_name, vehicle_model_name, vehicle_color, vehicle_price, seat_capacity,
                 quantity):
        """ This inherits the attributes of its parent class Vehicle"""
        super().__init__(vehicle_type, vehicle_name, vehicle_model_name, vehicle_color, vehicle_price, quantity)
        self.seat_capacity = seat_capacity

    def description(self):
        return f'This car {self.vehicle_name} of model {self.vehicle_model_name} is manufactured in' \
               f' {self.vehicle_manufactured_at}'

    def __del__(self):
        return 'Instance deleted'

    # @staticmethod
    # def calculate_tax(price, c_gst, s_gst):
    #     total_price = (c_gst * price) + (s_gst * price)
    #     return f'The total tax for the car {total_price}'


# audi = Car('4-wheeler', 'Audi', 'E-5', 'Black', '30L', '2-seater')


class Truck(Vehicle):

    def __init__(self, vehicle_type, vehicle_name, vehicle_model_name, vehicle_color, vehicle_price, quantity, mileage):
        super().__init__(vehicle_type, vehicle_name, vehicle_model_name, vehicle_color, vehicle_price, quantity)
        self.mileage = mileage

    def description(self):
        return f'This Truck is manufactured in {Truck.vehicle_manufactured_at}'

    def __del__(self):
        return 'Instance deleted'


class Pricing(Car, Truck):

    def __init__(self, vehicle_type, vehicle_name, vehicle_model_name, vehicle_color, vehicle_price, seat_capacity,
                 quantity):
        super().__init__(vehicle_type, vehicle_name, vehicle_model_name, vehicle_color, vehicle_price, seat_capacity,
                         quantity)

    def description(self):
        return f'This vehicle is manufactured at {Pricing.vehicle_manufactured_at}'

    def __del__(self):
        return 'Instance deleted'


print('Truck: ', Truck.mro())
print('pricing: ', Pricing.mro())

buying_price = Pricing
print('desc: ', buying_price.description)
print('desc 2 ', buying_price.mro())
print('pricing: ', buying_price.calculate_tax(10000, 1.5, 2.5))
print('car_manufactured_at 1: ', buying_price.vehicle_manufactured_at)
buying_price.vehicle_manufactured_at = 'Germany'
print('car_manufactured_at 2: ', buying_price.vehicle_manufactured_at)

audi = Car('4-wheeler', 'Audi', 'Electron-5', 'Black', 300000, '2-seater', '1')
audi.set_discount(0.25)
print('audi price: ', audi.get_price())

bmw = Car('4-wheeler', 'BMW', 'Class A-4', 'Silver', 250000, '2-seater', '2')
bmw.set_discount(.030)
print('bmw price: ', bmw.get_price())

tesla = Car(vehicle_name='Tesla', vehicle_model_name='Tesla v-6', vehicle_type='4-wheeler', vehicle_color='grey',
            vehicle_price=250000, quantity='2', seat_capacity='4-seater')

print(bmw)



