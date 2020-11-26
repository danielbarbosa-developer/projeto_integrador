import random

class past_wins():
    print("Bem vindo ao Game!")

    circuit = 0
    circuits_list = ["Interlagos","Monza","Suzuka"]

    while(circuit<=(len(circuits_list)-1)):
        print("Bem vindo ao circuito de "+ circuits_list[circuit])
        races = random.randrange(100)
        wins = random.randrange(100)
        while wins>races:
            wins = random.randrange(100)
        print("Na pista de "+circuits_list[circuit]+" vencemos "+str(wins)+" corridas de um total de "+str(races)+" corridas")
        print("Qual a chance de vercermos novamente aqui?")
        result = round((int(wins)*100)/int(races), 2)
        response = float(input("Digite aqui..."))
        if(result == response):
            print("Obrigado por sua análise, você acertou!")
        else:
            print("Nossos computadores mostram outra probabilidade, você errou")
        circuit += 1