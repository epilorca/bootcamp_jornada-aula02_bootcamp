import math
# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
"""
num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
result = num_1 + num_2

#print(f"A soma dos números inseridos é {result}")
"""
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
"""
numero = int(input("Digite um número: "))
result = numero % 5

print(f"O resto da divisão por 5 é {result}")
"""
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
result = num1 * num2

print(F"o resultado da multiplicação dos 2 números é {result}.")
"""
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
result = num1 // num2

print(f"O resultado da divisão é {result}")
"""
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
"""
numero = int(input("Digite o número: "))
result = numero ** 2

print(f"O resultado do número {numero} ao quadrado é {result}")
"""
# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
result = num1 + num2

print(f"O resultado da adição dos números flutuantes é {result}")
"""

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
result = (num1 + num2) / 2

print(f"O resultado do cálculo é {result}")
"""

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
"""
base = float(input("Digite o valor da base: "))
expoente = float(input("Digite o valor do expoente: "))
calc = base ** expoente

print(f"O resultado do cálculo é {calc}")
"""

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
"""
celsius = float(input("Digite a temperatura em Celsius: "))
farenheit = (celsius * 9/5) + 32
print(f"A conversão de {celsius} graus Celsius para Farenheit é {farenheit}")
"""
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio = float(input("Digite o raio do círculo para o cálculo: "))
area = math.pi * (raio ** 2)

print(f"A área do círculo é {area:.2f} cm quadrados")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
"""
palavra = input("Digite uma palavra: ")
if palavra.isdigit():
    print("Você digitou a palavra errada.")
    exit()
elif len(palavra) == 0:
    print("Você não digitou a palavra.")
    exit()
elif palavra.isspace():
    print("Você digitou somente espaço.")
    exit()
result = palavra.upper()

print(f"A palavra digitada se converte, ficando assim: {result}")
"""
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
"""
nome = input("Digite seu nome completo: ")
if nome.isdigit():
    print("Você digitou seu nome errado.")
    exit()
elif len(nome) == 0:
    print("Você não digitou seu nome.")
    exit()
elif nome.isspace():
    print("Você digitou somente espaço.")
    exit()
result = nome.lower()

print(f"O seu nome converido fica assim: {result}")
"""
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
"""
frase = input("Digite uma frase com espaçamento fora do padrão entre palavras: ").strip()
frase_corigida = " ".join(frase.split())
frase_final = frase_corigida.replace(" .", ".")

print(f"O resultado da frase é '{frase_final}'")
"""

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
"""
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")

print(f"Dia: {dia}")
print(f"Mês: {mes}")
print(f"Ano: {ano}")
"""
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
"""
string1 = input("Digite a primeira palavra: ")
string2 = input("Digite a segunda palavra: ")
result = string1 + " " + string2
print(f"O resultado é: {result}")
"""

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação