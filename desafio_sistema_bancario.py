Saque_limite_diario = 1500
limite_por_saque = 500
extrato = ''
saldo_conta = 10000

while True:
    menu = input('Selecione a opção desejada: \n\n[D]Depósito \n[E]Extrato \n[S]Saldo \n[F]Finalizar: ').upper() 

    if menu == "D": 
        deposito_em_conta = int(input("Digite o valor do depósito: "))  
        saldo_conta += deposito_em_conta  
        extrato += f'Depósito: {deposito_em_conta}\n' 
        print(f"Você depositou {deposito_em_conta}. Saldo atual: R$ {saldo_conta}")  

    elif menu == "E":
        extrato += f'Saldo atual: {saldo_conta}\n'  
        print(f'Extrato:\n{extrato}')  

    elif menu == "S":
        print(f'O saldo atualizado de sua conta é R$: {saldo_conta}')

    elif menu == "F":
        print('Muito obrigada por utilizar nossos serviços! Estamos sempre à disposição!')
        break  
