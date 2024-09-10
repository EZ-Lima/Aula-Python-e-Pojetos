print("Vamos calcular seu IMC")
nome = 'Eliezer Lima'
altura = 1.77
peso = 87
imc = peso / (altura ** 2)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} e seu IMC é {imc:.2f}'
print(linha_1)
print(linha_2)