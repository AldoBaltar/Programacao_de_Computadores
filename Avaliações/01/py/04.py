velocidade = float(input("digite o valor do vento: "))

if velocidade == 0:
    print("Sem Vento.")

elif velocidade > 0 and velocidade < 20:
    print("Vento Fraco.")

elif velocidade >= 20 and velocidade < 50:
    print("Vento Moderado.")

elif velocidade >= 50:
    print("Vento Forte.")
    
else:
    print("Invalido.")