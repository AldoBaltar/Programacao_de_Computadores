peso = float(input('Digite o peso da bagagem: '))
dias_antecedencia = int(input('Digite os dias de antecedência: '))

if peso <= 10 and dias_antecedencia >= 7:
    print('Bagagem gratuita')

elif peso < 10 and dias_antecedencia < 7:
    print('Taxa de R$50,00')

elif peso > 10 and peso < 23:
    print('Taxa de R$120,00')

else:
    print('Taxa de R$250,00 -- excesso de bagagem')