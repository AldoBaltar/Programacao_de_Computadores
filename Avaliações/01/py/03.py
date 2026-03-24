valor = float(input('Digite o valor do produto: '))
categoria = str(input('Digite a categoria do produto: '))

if valor > 2000 and categoria == 'premium': 
    print('Garantia estendida de 3 anos')
    
elif valor > 0 and valor <= 2000 and categoria == 'premium':
    print('Garantia estendida de 2 anos')

else: 
    print('Garantia padrão de 1 ano')