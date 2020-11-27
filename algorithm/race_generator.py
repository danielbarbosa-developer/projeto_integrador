import random
import pandas as pd

class race_generator():

    def formula_one_random_values(numero_de_carros):
    data_frame = pd.DataFrame()
    for carro in range(numero_de_carros):
        data_frame['aceleracao_{}'.format(carro)] = [random.randint(1,10) for velocidades in range(200)]
        data_frame['velocidade_inicial_{}'.format(carro)] = [random.randint(90,150) for velocidades in range(200)]

    return data_frame, data_frame.describe()


