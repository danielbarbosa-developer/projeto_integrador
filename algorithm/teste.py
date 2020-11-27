from car_performance_generator import car_performance
from past_wins_generator import past_wins

car = car_performance(5)
print(car.velocity())

past = past_wins()
print(past.define_past_wins())
