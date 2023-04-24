class Car:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX = Car(240,18)
print(f'the max spped of modelX is {modelX.max_speed},the mile age of modelX is  {modelX.mileage}')