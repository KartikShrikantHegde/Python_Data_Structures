# class Car(object):
#     condition = "new"
#
#     def __init__(self, model, color, mpg):
#         self.model = model
#         self.color = color
#         self.mpg   = mpg
#
# class ElectricCar(Car):
#     def __init__(self, battery_type, model, color, mpg):
#         self.battery_type=battery_type
#         super(ElectricCar, self).__init__(model, color, mpg)
#
# car = ElectricCar('battery', 'ford', 'golden', 10)
# print car.__dict__

class Car(object)
