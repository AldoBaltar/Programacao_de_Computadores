imc = float(input('Digite o IMC: '))

if imc == 0:
    print('O número zero é invalido')

elif imc >= 30:
    print('Obesidade')

elif imc >= 25 and imc <= 29.9:
    print('Sobrepeso')

elif imc >= 18.5 and imc <= 24.9:
    print('Peso normal')

else:
    print('Abaixo do peso')