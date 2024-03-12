#!/usr/bin/env python
# coding: utf-8

# In[ ]:


''' Checkpoint 1 - Primeiro semestre 2024
    Disciplina - COMPUTATIONAL THINKING USING PYTHON
'''

'''--------------------------------------------------------------------------------------'''


# Exercício 1 (2 Pontos)
''' Faça a atribuição de 4 tipos de variável no Python,
    complentando o código abaixo:
'''

# Item A
''' Faça a atribuição de um número inteiro de valor 10'''
# Descomente e complete o código a seguir:

var_N_inteiro = 10 


# Item B
''' Faça a atribuição de um número de ponto flutuante (float),
    de valor 5
'''
# Descomente e complete o código a seguir:

var_N_pFlutuante = 5.0


# Item C
''' Faça a atribuição de uma "string" 
    com a seguinte frase: "A soma dos valores é: " 
'''
# Descomente e complete o código a seguir:

var_string = "A soma dos valores é: "


# Item D
''' Faça a atribuição de uma variável boleana, de valor "verdadeiro" '''
# Descomente e complete o código a seguir:

var_boleana = True


'''--------------------------------------------------------------------------------------'''


# Exercício 2 (2 Pontos)
''' Utilize as 4 operações basicas (soma, subtração, multiplicação e divisão):
'''

# Item A
''' Some a variável com número inteiro, 
    atribuída no exercício anterior, 
    com o número 20
'''
# Descomente e complete o código a seguir:

var_soma = var_N_inteiro + 20


# Item B
''' Multiplique a variável com número de ponto flutuante, 
    atribuída no exercício anterior, 
    pelo número 10
'''
# Descomente e complete o código a seguir:

var_multiplicacao = var_N_pFlutuante * 10


# Item C
''' Subtraia a variável soma, 
    atribuída neste mesmo exercício, 
    pelo número 10
'''
# Descomente e complete o código a seguir:

var_subtracao = var_soma - 10


# Item D
''' Divida a variável subtracao, 
    atribuída neste mesmo exercício, 
    pelo número 10
'''
# Descomente e complete o código a seguir:

var_divisão = var_subtracao - 10



'''--------------------------------------------------------------------------------------'''


# Exercício 3 (1 Pontos)
''' Imprima a variável "string" criada n o exercício 1:
'''

'''Siga o modelo apresentado abaixo: '''
#função_de_impressão(variável_a_imprimir)

print(var_string)

'''--------------------------------------------------------------------------------------'''


# Exercício 4 (1 Pontos)
''' Faça um "input" na variável abaixo, 
    com o valor de 100, pelo terminal
'''

''' Lembrem-se que a função de "inpu" pode ter um texto 
    para apresentar no terminal, mas não é obrigatório'''
# Descomente e complete o código a seguir:
var_input = input()


'''--------------------------------------------------------------------------------------'''


# Exercício 5 (1 Pontos)
''' Faça um "Casting" (conversão) da variável "input" do exercício anterior,
    de modo que a nova variável seja um número inteiro:
'''

'''Siga o modelo apresentado abaixo: '''
# Descomente e complete o código a seguir:
var_input_casting_inteiro = int(var_input)


'''--------------------------------------------------------------------------------------'''


# Exercício 6 (1 Pontos)
''' imprima o tipo da variável do exercício anterior 
    (aquela que fizemos o "casting")
'''

'''Siga o modelo apresentado abaixo: '''
#função_tipo(variável_em_questão)

# Descomente e complete o código a seguir:
var_tipo_casting_inteiro = type(var_input_casting_inteiro)
print(var_tipo_casting_inteiro)


'''--------------------------------------------------------------------------------------'''


# Exercício 7 (2 Pontos)
''' Faça a multiplicação das variáveis: 
    "var_multiplicacao" e "var_divisão" e verifique se este valor
    é maior ou igual ao da variável "var_input_casting_inteiro" utilizando um 
    operador lógico que ateste se a multiplicação dos dois primeiros é 
    MAIOR OU IGUAL ao último. Faça a impressão deste valor na TELA.
'''

# Descomente e complete o código a seguir:
comparacao_valores = var_multiplicacao * var_divisão

comparacao_valores == var_input_casting_inteiro
comparacao_valores > var_input_casting_inteiro

print("O valor é igual" if comparacao_valores == var_input_casting_inteiro else "O valor é maior")
