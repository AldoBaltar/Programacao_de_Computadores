i = 1
qnt = 0

while i <=20:

    i += 1
    idade = int(input('Digite as idades: '))

    if idade > 10 and idade < 20:
        qnt += 1

    else:
        print('Essa idade não está entre 10 e 20!')

print(f'Você tem {qnt} idades entre 10 e 20')