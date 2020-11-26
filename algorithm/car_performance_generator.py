import random

class car_performance():

    def __init__(self, cars):
        self.cars = cars
        
    def velocity(self):
        velocity_table = []
        #cars_number = cars_arrays
        cars_number = []
        for n in range(1,self.cars):
            cars_number.append(n)
        for n in cars_number:
            car_velocity_array = []
            car_velocity_array.append(n)
            car_velocity_array.append(random.randrange(300,380))
            velocity_table.append(car_velocity_array)
        return velocity_table





        
