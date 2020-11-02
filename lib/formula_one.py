import numpy as np
import pandas as pd

class formula_one():

    def __init__(self):
        self = self

    def generate_random_racing(self,number_of_cars):
        velocidade_media_carros_participantes = np.random.randint(150,250,(1000,number_of_cars))
        column_names = ["carro_"+ str((i+number_of_cars)) for i in range(10)]
        self.df = pd.DataFrame(velocidade_media_carros_participantes,columns = column_names)
        data_statistics = self.df.describe()
        return self.df, data_statistics
    


