import random

class past_wins():

    def define_past_wins(self):
        circuits_list = ["Interlagos","Monza","Suzuka"]
        past_wins_in_circuits = []

        for circuit in circuits_list:
            wins = random.randrange(15)
            circuit_with_wins = []
            circuit_with_wins.append(circuit)
            circuit_with_wins.append(wins)
            past_wins_in_circuits.append(circuit_with_wins)
        
        return past_wins_in_circuits






        
    