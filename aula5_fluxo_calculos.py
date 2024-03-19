# ===============================================================

##Exemplo 1

# n1 = eval(input('Digite o valor de n1: '))
# n2 = eval(input('Digite o valor de n2: '))

# med = (n1 + n2) / 2

# print(med)

# ===============================================================

# ##Exemplo 2

# # Desnecessário
# # km = float()
# # l = float()
# # autonomia = float()

# km = eval(input("Digite quantos km: "))
# l = eval(input("Digite quantos litros: "))

# autonomia = km / l
# arredondamento = round(autonomia,2)

# print(arredondamento)

# ===============================================================

# ##Exemplo 3

# quantia = eval(input("Digite o valor desejado: "))
# ced50 = quantia // 50

# quantia = quantia % 50

# ced20 = quantia  // 20

# quantia = quantia %  20

# ced10 = quantia // 10

# quantia = quantia % 10

# print(quantia)
# print(f'{ced50} nota(s) de R$50, {ced20} nota(s) de R$20, {ced10} nota(s) de R$10')


# ===============================================================


# # Exercicio 1
# #Fazer um algoritmo que alcule a média de 4 números dados pelo usuário
# n1 = eval(input("Digite o n1: "))
# n2 = eval(input("Digite o n2: "))
# n3 = eval(input("Digite o n3: "))
# n4 = eval(input("Digite o n4: "))

# media = (n1 + n2 + n3 + n4) / 4
# print(f"A media é igual a {media}")


# ===============================================================

# # Exercício 2
# # Dada a quilometragem parcial de um carro e a quantidade de litros gastos por um carro para percorrer esta quilometragem, fazer um algoritmo que calcule quantos Km/l o carro percorreu.

# km = eval(input("Informe a quilometragem: "))
# l = eval(input("Informe quantos litros: "))

# resultado = km / l

# resultadoArredondado = round(resultado,2)
# print(f'{resultadoArredondado}')


# ===============================================================


# Exercicio 3
# Dado o preço do maço de cigarros, a quantidade de maços consumidos por dia e o temp em anos que a pessoa fuma, calcular o quanto esta pessoa já gastou fumando.

preco = eval(input("Informe o preço do maço de cigarro: "))
qtd_macos = eval(input("Informe a quantidade de maços consumidos por dia: "))
anos = eval(input("Informe o tempo em anos que a pessoa fuma: "))

# calculo anos em dias
dias_totais = 365 * anos

gastos = round(((preco * qtd_macos) * dias_totais),2)

print(f'{gastos}')
