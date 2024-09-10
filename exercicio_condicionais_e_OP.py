primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

condicao1 = primeiro_valor > segundo_valor
condicao2 = primeiro_valor < segundo_valor

if condicao1:
    print('O número:',primeiro_valor,  'é maior que o número:',segundo_valor)

elif condicao2:
    print('O número:',primeiro_valor, 'é menor que o número:',segundo_valor )

else:
    print('Os dois valores são iguais')