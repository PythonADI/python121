class Car:
    def __init__(self, make, model, unlocked_features = False):
        # method is a function that belongs to a class and object
        self.make = make
        self.model = model
        self.unlocked_features = unlocked_features

    def describe(self):
        # method that belongs to an object
        print(f"Make: {self.make}\nModel: {self.model}\nFeatures Are Unlocked: {self.unlocked_features}")

my_car = Car("Tesla", "Model S3")
# print(my_car.make, my_car.model, my_car.unlocked_features)
my_car.describe()

my_car_2 = Car("BMW", "X5", True)
my_car_2.describe()
