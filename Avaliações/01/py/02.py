score = float(input("digite o valor do seu Score: "))
renda = float(input("digite o valor da sua Renda Mensal: "))

if score > 700 and renda > 3000:
    print("Empréstimo Concedido Automaticamente.")

else:
    print("Empréstimo Negado devido Score e/ou Renda Mensal insuficiente. Procure um Gerente.")